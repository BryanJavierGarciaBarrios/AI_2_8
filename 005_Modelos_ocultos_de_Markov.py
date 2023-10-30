pip install hmmlearn

from hmmlearn import hmm
import numpy as np

# Definir los estados ocultos y las observaciones
states = ["Soleado", "Lluvioso"]
n_states = len(states)

observations = [0, 1, 0, 0, 1, 1, 0, 0, 0, 1]
obs = np.array(observations).reshape(-1, 1)

# Crear un modelo HMM
model = hmm.MultinomialHMM(n_components=n_states)

# Entrenar el modelo (en este ejemplo, usamos un conjunto de datos de entrenamiento fijo)
model.fit(obs)

# Establecer las probabilidades iniciales
model.startprob_ = np.array([0.6, 0.4])

# Establecer las probabilidades de transición entre estados
model.transmat_ = np.array([[0.7, 0.3],
                            [0.4, 0.6]])

# Establecer las probabilidades de emisión (en este ejemplo, asumimos distribuciones multinomiales)
model.emissionprob_ = np.array([[0.8, 0.2],
                               [0.3, 0.7]])

# Predecir la secuencia más probable de estados ocultos
predicted_states = model.predict(obs)

print("Secuencia de estados ocultos predichos:")
for i in predicted_states:
    print(states[i])
