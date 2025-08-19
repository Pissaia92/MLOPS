# airflow/dags/dag_etl_imoveis.py
from airflow import DAG
from airflow.operators.python import PythonOperator  # ✅ Import correto
from datetime import datetime
import os

# Não use polars no container ainda — use pandas (já vem com Airflow)
import pandas as pd

def extrair():
    os.makedirs("/opt/airflow/dags/data", exist_ok=True)
    df = pd.DataFrame({
        "area": [50, 70, 80, 60, 90],
        "quartos": [2, 3, 3, 2, 4],
        "bairro": ["A", "B", "A", "C", "B"],
        "preco": [300000, 450000, 500000, 350000, 600000]
    })
    df.to_parquet("/opt/airflow/dags/data/raw_imoveis.parquet")

def carregar():
    from sqlalchemy import create_engine
    engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres:5432/airflow")
    df = pd.read_parquet("/opt/airflow/dags/data/raw_imoveis.parquet")
    df.to_sql("imoveis", engine, if_exists="replace", index=False)

with DAG(
    "etl_imoveis",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@once",
    catchup=False
) as dag:
    extrair_task = PythonOperator(task_id="extrair", python_callable=extrair)
    carregar_task = PythonOperator(task_id="carregar", python_callable=carregar)
    extrair_task >> carregar_task