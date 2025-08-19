# api/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Inicializar a aplicação FastAPI
app = FastAPI(title="API de Previsão de Preços de Imóveis")

class ModeloSimulado:
    def predict(self, X):
        # Simulação: preço = area * 6000 + quartos * 10000
        return np.array([x[0] * 6000 + x[1] * 10000 for x in X])

model = joblib.load("mlflow/modelo_preco.pkl")

# Definir o modelo de dados de entrada
class DadosImovel(BaseModel):
    area: float
    quartos: int

# Endpoint de predição
@app.post("/predict")
def predict_price(dados: DadosImovel):
    """
    Prevê o preço de um imóvel com base na área e número de quartos.
    """
    # Preparar os dados para predição
    features = np.array([[dados.area, dados.quartos]])
    
    # Fazer a predição
    preco_previsto = model.predict(features)[0]
    
    return {
        "area": dados.area,
        "quartos": dados.quartos,
        "preco_previsto": round(preco_previsto, 2)
    }

# Endpoint de health check
@app.get("/")
def read_root():
    return {"message": "API de Previsão de Preços de Imóveis está rodando!"}