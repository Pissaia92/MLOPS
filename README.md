## MLOps Project - Real Estate Price Prediction

This project implements a complete MLOps pipeline for real estate price prediction, demonstrating skills in data engineering, machine learning, and deployment.

## Objective

Create an end-to-end system that:
1. Collects and processes data (ETL).
2. Transforms and models the data.
3. Trains and version a machine learning model.
4. Exposes the model via a REST API.
5. Provides a visual interface for interaction and monitoring.

## Architecture

[Simulated Data] → [Airflow (ETL)] → [PostgreSQL]

↓

[dbt (Transformation)] → [ML Model (Scikit-learn)]

↓

[FastAPI (API)] → [Evidently (Monitoring)]

↓

[Streamlit (Dashboard)]

## Technologies

- **Orchestration/ETL:** Apache Airflow
- **Data Transformation:** dbt (data build tool)
- **Database:** PostgreSQL (Docker)
- **Processing:** Polars, Pandas
- **Machine Learning:** Scikit-learn
- **MLOps/Versioning:** MLflow
- **API:** FastAPI
- **Monitoring:** Evidently AI
- **Visualization:** Streamlit
- **Infrastructure:** Docker, Docker Compose
- **Language:** Python

## How to Run Locally

**Prerequisites:**
- Docker and Docker Compose installed.
- Python 3.8+ and `venv` configured.

1. **Clone the repository:**
```bash
git clone <YOUR_REPOSITORY_URL>
cd mlops-real-estate-project
```
2. **Start the services with Docker:**
```bash
docker-compose up -d
```
3. **Access Airflow:**
- URL: http://localhost:8080
- Login: `airflow` / `airflow`
- Run the DAG `etl_real-estate` to load the simulated data. 4. **(Optional) Train the model (already included as an example):**
- The model was trained within the Airflow container and saved in `mlflow/modelo_preco.pkl`. - If you need to retrain, access the container:
```bash
docker exec -it project_airflow bash
python /opt/airflow/dags/train_model_in_container.py
```
5. **Install the dependencies for the API and Dashboard:**
```bash
# Activate your Python virtual environment
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
6. **Copy the model (if retrained):**
```bash
docker cp project_airflow:/opt/airflow/dags/modelo_preco.pkl mlflow/
```
7. **Run the API with FastAPI:**
```bash
uvicorn api.main:app --reload --port 8000
```
- Access the interactive documentation: http://localhost:8000/docs
8. **Run the dashboard with Streamlit:** 
```bash 
streamlit run dashboard/app.py 
```
