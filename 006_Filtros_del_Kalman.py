pip install filterpy
from filterpy.kalman import KalmanFilter
import numpy as np
import matplotlib.pyplot as plt

# Definir el modelo del filtro de Kalman
kf = KalmanFilter(dim_x=1, dim_z=1)

# Definir la matriz de transición de estado (A)
kf.F = np.array([[1.]])

# Definir la matriz de observación (H)
kf.H = np.array([[1.]])

# Definir la matriz de covarianza del proceso (Q)
kf.Q = np.array([[0.01]])

# Definir la matriz de covarianza de la medición (R)
kf.R = np.array([[0.1]])

# Definir la estimación inicial y su covarianza
kf.x = np.array([0.])
kf.P = np.array([[1.])

# Simular una secuencia de observaciones ruidosas
observaciones = [1.2, 1.4, 1.6, 1.8, 2.0]

# Realizar la estimación del estado a partir de las observaciones
estimaciones = []

for z in observaciones:
    kf.predict()
    kf.update(z)
    estimaciones.append(kf.x[0])

# Graficar las observaciones y las estimaciones
plt.plot(observaciones, label='Observaciones', marker='o')
plt.plot(estimaciones, label='Estimaciones', marker='x')
plt.legend()
plt.title('Filtro de Kalman')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.grid(True)
plt.show()
