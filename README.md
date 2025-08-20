Real Estate Price Prediction 🏠

A comprehensive MLOps project for real estate price prediction. Implements a data pipeline from ETL to visualization, demonstrating skills in data engineering, machine learning, and deployment.

📌 Objective

Build an end-to-end system that collects, processes, and transforms data, trains machine learning models, and delivers real-time predictions via API and dashboard.

🛠️ Technologies

Orchestration/ETL: Apache Airflow

Data Transformation: dbt (data build tool)

Database: PostgreSQL (Docker)

Processing: Polars, Pandas

Machine Learning: Scikit-learn

MLOps/Versioning: MLflow

API: FastAPI

Monitoring: Evidently AI

Visualization: Streamlit

Infrastructure: Docker, Docker Compose

Language: Python

✨ Architecture

ETL (Airflow) → collect and load data into PostgreSQL

Transformation (dbt) → cleaning and modeling

Training (Scikit-learn + MLflow) → model versioning

API (FastAPI) → exposing the trained model

Monitoring (Evidently) → drift and performance metrics

Dashboard (Streamlit) → visualization and interaction with the model
