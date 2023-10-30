import numpy as np

# Definir el modelo oculto de Markov (HMM)
# En este ejemplo, usaremos un HMM simple con 2 estados (S1 y S2) y 3 observaciones (O1, O2 y O3).
num_estados = 2
num_observaciones = 3

# Probabilidades iniciales de los estados
pi = np.array([0.6, 0.4])

# Matriz de transición de estados
transiciones = np.array([[0.7, 0.3],
                        [0.4, 0.6]])

# Matriz de emisión de observaciones
emisiones = np.array([[0.1, 0.4, 0.5],
                     [0.6, 0.3, 0.1]])

# Secuencia de observaciones
observaciones = [0, 1, 2]  # Por ejemplo, O1, O2, O3

# Algoritmo hacia adelante
def forward_algorithm(pi, transiciones, emisiones, observaciones):
    T = len(observaciones)
    alpha = np.zeros((T, num_estados))

    # Paso inicial
    alpha[0] = pi * emisiones[:, observaciones[0]]

    # Pasos recursivos
    for t in range(1, T):
        for j in range(num_estados):
            alpha[t, j] = np.sum(alpha[t - 1] * transiciones[:, j]) * emisiones[j, observaciones[t]]

    return alpha

# Algoritmo hacia atrás
def backward_algorithm(transiciones, emisiones, observaciones):
    T = len(observaciones)
    beta = np.zeros((T, num_estados))

    # Paso final
    beta[-1] = 1

    # Pasos recursivos
    for t in range(T - 2, -1, -1):
        for i in range(num_estados):
            beta[t, i] = np.sum(transiciones[i, :] * emisiones[:, observaciones[t + 1]] * beta[t + 1, :])

    return beta

# Calcular la probabilidad de la secuencia de observaciones
alpha = forward_algorithm(pi, transiciones, emisiones, observaciones)
beta = backward_algorithm(transiciones, emisiones, observaciones)
probabilidad = np.sum(alpha[-1] * beta[0])

print("Probabilidad de la secuencia de observaciones:", probabilidad)
