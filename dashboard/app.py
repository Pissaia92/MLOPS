import streamlit as st
import pandas as pd

st.title("📊 Dashboard de Monitoramento do Modelo")
st.write("Este é um dashboard de exemplo para o projeto MLOps.")

# Métricas simuladas
st.header("Métricas do Modelo")
col1, col2, col3 = st.columns(3)
col1.metric("R²", "0.95")
col2.metric("RMSE", "15000")
col3.metric("Drift", "Baixo")

# Gráfico de exemplo
st.header("Performance ao Longo do Tempo")
chart_data = pd.DataFrame({
    'Dia': range(1, 8),
    'R²': [0.95, 0.94, 0.96, 0.93, 0.95, 0.94, 0.96]
})
st.line_chart(chart_data.set_index('Dia'))