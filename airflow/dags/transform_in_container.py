import pandas as pd
from sqlalchemy import create_engine

# Conectar ao PostgreSQL (dentro do container, usamos o nome do serviço)
engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres:5432/airflow")

# Ler dados brutos
df_raw = pd.read_sql("SELECT * FROM imoveis", engine)

# Transformar (mesmo cálculo do dbt)
df_transformed = df_raw.copy()
df_transformed["preco_por_m2"] = df_transformed["preco"] / df_transformed["area"]

# Salvar tabela transformada
df_transformed.to_sql(
    "stg_imoveis",
    engine,
    schema="dbt_imoveis",
    if_exists="replace",
    index=False
)

print("✅ Dados transformados e salvos em dbt_imoveis.stg_imoveis")