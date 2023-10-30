import numpy as np
import matplotlib.pyplot as plt

# Semilla para la reproducibilidad
np.random.seed(0)

# Generar una serie temporal de ruido blanco
n_samples = 1000
white_noise = np.random.normal(0, 1, n_samples)  # Media 0 y desviación estándar 1

# Crear un vector de tiempo
time = np.arange(n_samples)

# Calcular la media y la varianza a lo largo del tiempo
mean_values = [np.mean(white_noise[:i+1]) for i in range(n_samples)]
variance_values = [np.var(white_noise[:i+1]) for i in range(n_samples)]

# Graficar la serie temporal de ruido blanco
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, white_noise, label='Ruido Blanco')
plt.title('Serie Temporal de Ruido Blanco')
plt.xlabel('Tiempo')
plt.ylabel('Valor')

# Graficar la evolución de la media y la varianza a lo largo del tiempo
plt.subplot(2, 1, 2)
plt.plot(time, mean_values, label='Media')
plt.plot(time, variance_values, label='Varianza')
plt.legend()
plt.title('Evolución de la Media y la Varianza')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.tight_layout()
plt.show()
