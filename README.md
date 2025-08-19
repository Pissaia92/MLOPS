Projeto MLOps - Previsão de Preços de Imóveis

Este projeto implementa um pipeline completo de MLOps para prever preços de imóveis, demonstrando habilidades em engenharia de dados, machine learning e deploy.

## 🎯 Objetivo

Criar um sistema end-to-end que:
1.  Coleta e processa dados (ETL).
2.  Transforma e modela os dados.
3.  Treina e versiona um modelo de machine learning.
4.  Expõe o modelo via uma API REST.
5.  Oferece uma interface visual para interação e monitoramento.

## 🧱 Arquitetura

[Dados Simulados] → [Airflow (ETL)] → [PostgreSQL]
↓
[dbt (Transformação)] → [Modelo ML (Scikit-learn)]
↓
[FastAPI (API)] → [Evidently (Monitoramento)]
↓
[Streamlit (Dashboard)]


## 🛠️ Tecnologias

- **Orquestração/ETL:** Apache Airflow
- **Transformação de Dados:** dbt (data build tool)
- **Banco de Dados:** PostgreSQL (Docker)
- **Processamento:** Polars, Pandas
- **Machine Learning:** Scikit-learn
- **MLOps/Versionamento:** MLflow
- **API:** FastAPI
- **Monitoramento:** Evidently AI
- **Visualização:** Streamlit
- **Infraestrutura:** Docker, Docker Compose
- **Linguagem:** Python

## ▶️ Como Rodar Localmente

**Pré-requisitos:**
- Docker e Docker Compose instalados.
- Python 3.8+ e `venv` configurado.

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd projeto-mlops-imoveis
    ```
2.  **Inicie os serviços com Docker:**
    ```bash
    docker-compose up -d
    ```
3.  **Acesse o Airflow:**
    - URL: http://localhost:8080
    - Login: `airflow` / `airflow`
    - Execute o DAG `etl_imoveis` para carregar os dados simulados.
4.  **(Opcional) Treine o modelo (já incluso como exemplo):**
    - O modelo foi treinado dentro do container do Airflow e salvo em `mlflow/modelo_preco.pkl`.
    - Se precisar re-treinar, acesse o container:
     ```bash
     docker exec -it projeto_airflow bash
     python /opt/airflow/dags/train_model_in_container.py
     ```
5.  **Instale as dependências para a API e o Dashboard:**
    ```bash
    # Ative seu ambiente virtual Python
    python -m venv venv
    source venv/bin/activate # No Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
6.  **Copie o modelo (se re-treinado):**
    ```bash
     docker cp projeto_airflow:/opt/airflow/dags/modelo_preco.pkl mlflow/
    ```
7.  **Rode a API com FastAPI:**
    ```bash
    uvicorn api.main:app --reload --port 8000
    ```
    - Acesse a documentação interativa: http://localhost:8000/docs
8.  **Rode o dashboard com Streamlit:**
    ```bash
    streamlit run dashboard/app.py
    ```