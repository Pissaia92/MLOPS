# train_model_in_container.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import mlflow
import mlflow.sklearn
from sqlalchemy import create_engine

# Conectar ao PostgreSQL (dentro do container, usamos o nome do serviço)
engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres:5432/airflow")

# Ler dados transformados
with engine.connect() as conn:
    df = pd.read_sql("SELECT area, quartos, preco FROM dbt_imoveis.stg_imoveis", conn)

# Preparar dados
X = df[["area", "quartos"]]
y = df["preco"]

# Treinar modelo
model = LinearRegression()
model.fit(X, y)

# Registrar no MLflow (se estiver rodando)
# mlflow.set_tracking_uri("http://mlflow:5000")  # Nome do serviço Docker
# mlflow.set_experiment("preco_imoveis")

# with mlflow.start_run():
#     mlflow.sklearn.log_model(model, "modelo_preco")
#     mlflow.log_params({"modelo": "LinearRegression"})
#     mlflow.log_metric("r2", model.score(X, y))
#     print("✅ Modelo treinado e registrado no MLflow!")

# Salvar modelo localmente (no container)
joblib.dump(model, "/opt/airflow/dags/modelo_preco.pkl")
print("✅ Modelo treinado e salvo em /opt/airflow/dags/modelo_preco.pkl")