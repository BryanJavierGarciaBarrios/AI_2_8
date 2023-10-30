import numpy as np

# Matriz de transición de la cadena de Markov
# Cada fila representa las probabilidades de transición desde un estado
# Las filas deben sumar 1
matriz_transicion = np.array([[0.7, 0.3],
                              [0.2, 0.8]])

# Estado inicial
estado_actual = 0

# Número de pasos a simular
num_pasos = 20

# Lista para almacenar la secuencia de estados
secuencia_estados = [estado_actual]

# Simulación de la cadena de Markov
for _ in range(num_pasos):
    # Generar un estado siguiente a partir de la matriz de transición
    estado_siguiente = np.random.choice([0, 1], p=matriz_transicion[estado_actual])
    secuencia_estados.append(estado_siguiente)
    estado_actual = estado_siguiente

# Imprimir la secuencia de estados
print("Secuencia de Estados:")
print(secuencia_estados)
