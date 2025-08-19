# mlflow/train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import mlflow
import mlflow.sklearn
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection

# Conectar ao PostgreSQL (do host, usando localhost)
DATABASE_URL = "postgresql+psycopg2://airflow:airflow@172.18.0.3:5432/airflow"
engine = create_engine(DATABASE_URL)

conn: Connection
with engine.connect() as conn:
    df = pd.read_sql("SELECT area, quartos, preco FROM dbt_imoveis.stg_imoveis", conn)

# Preparar dados
X = df[["area", "quartos"]]
y = df["preco"]

# Treinar modelo
model = LinearRegression()
model.fit(X, y)

# Registrar no MLflow
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("preco_imoveis")

with mlflow.start_run():
    mlflow.sklearn.log_model(model, "modelo_preco")
    mlflow.log_params({"modelo": "LinearRegression"})
    mlflow.log_metric("r2", model.score(X, y))
    print("✅ Modelo treinado e registrado no MLflow!")

# Salvar modelo localmente
joblib.dump(model, "mlflow/modelo_preco.pkl")