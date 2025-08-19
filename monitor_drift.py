import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
from evidently.metric_preset import TargetDriftPreset
from sklearn.model_selection import train_test_split

# Gerar dados de exemplo para simular referência e atual
data = pd.DataFrame({
    'area': [50, 60, 70, 80, 90, 100],
    'quartos': [2, 2, 3, 3, 4, 4],
    'preco': [300000, 350000, 450000, 500000, 600000, 650000]
})

# Dividir em referência e atual (simulando)
reference_data, current_data = train_test_split(data, test_size=0.5, random_state=42)

# Criar relatório de drift
report = Report(metrics=[
    DataDriftPreset(),
    TargetDriftPreset()
])

report.run(reference_data=reference_data, current_data=current_data)
report.save_html("drift_report.html")

print("✅ Relatório de drift salvo em drift_report.html")