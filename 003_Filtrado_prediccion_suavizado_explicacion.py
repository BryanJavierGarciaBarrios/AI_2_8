import numpy as np

# Datos de ejemplo (serie temporal)
data = [23, 27, 30, 33, 37, 41, 45, 48, 52, 56]

# Parámetros del suavizado exponencial
alpha = 0.2  # Factor de suavizado (0 < alpha < 1)

# Inicialización
smoothed_data = [data[0]]  # El primer valor es igual al dato original

# Aplicación del suavizado exponencial
for i in range(1, len(data)):
    # Fórmula del suavizado exponencial simple
    smoothed_value = alpha * data[i] + (1 - alpha) * smoothed_data[-1]
    smoothed_data.append(smoothed_value)

# Predicción a futuro
forecast_steps = 3
forecasted_data = []
for i in range(forecast_steps):
    # En el suavizado exponencial simple, la predicción es igual al último valor suavizado
    forecasted_data.append(smoothed_data[-1])
    # Actualización de la serie suavizada con la predicción
    smoothed_value = alpha * forecasted_data[-1] + (1 - alpha) * smoothed_data[-1]
    smoothed_data.append(smoothed_value)

# Imprimir los resultados
print("Datos originales:", data)
print("Serie suavizada:", smoothed_data)
print(f"Predicción a {forecast_steps} pasos en el futuro:", forecasted_data)
