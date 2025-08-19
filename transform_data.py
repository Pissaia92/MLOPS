# transform_data.py
import polars as pl
from sqlalchemy import create_engine

# Conectar ao PostgreSQL
engine = create_engine("postgresql+psycopg2://airflow:airflow@localhost:5432/airflow")

# Ler dados brutos
df_raw = pl.read_database("SELECT * FROM imoveis", engine)

# Transformar (mesmo cálculo do dbt)
df_transformed = df_raw.with_columns(
    (pl.col("preco") / pl.col("area")).alias("preco_por_m2")
)

# Salvar tabela transformada
df_transformed.to_pandas().to_sql(
    "stg_imoveis",
    engine,
    schema="dbt_imoveis",
    if_exists="replace",
    index=False
)

print("✅ Dados transformados e salvos em dbt_imoveis.stg_imoveis")