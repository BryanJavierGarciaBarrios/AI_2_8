import random

# Definir la función de transición de estado
def transition_model(state, noise_stddev=0.1):
    # El objeto se mueve con ruido aleatorio
    return state + random.gauss(0, noise_stddev)

# Definir la función de observación (likelihood)
def observation_model(true_state, observed_state, noise_stddev=0.1):
    # La observación tiene ruido aleatorio
    return (1.0 / (noise_stddev * (2 * 3.1416) ** 0.5)) * \
           (2.71828 ** (-0.5 * ((observed_state - true_state) / noise_stddev) ** 2))

# Definir el filtro de partículas
def particle_filter(num_particles, initial_state, observations, transition_noise, observation_noise):
    particles = [initial_state + random.gauss(0, 0.1) for _ in range(num_particles)]
    weights = [1.0] * num_particles

    for observation in observations:
        # Actualizar partículas y pesos
        for i in range(num_particles):
            particles[i] = transition_model(particles[i], transition_noise)
            weights[i] *= observation_model(observation, particles[i], observation_noise)

        # Normalizar los pesos
        total_weight = sum(weights)
        weights = [w / total_weight for w in weights]

        # Resampling: Muestreo basado en peso
        new_particles = []
        for _ in range(num_particles):
            choice = random.choices(particles, weights)[0]
            new_particles.append(choice)
        particles = new_particles

    # Estimación del estado final (media de las partículas)
    estimated_state = sum(particles) / num_particles

    return estimated_state

# Parámetros del problema
num_particles = 100
initial_state = 0.0
true_state = [initial_state]
observations = [0.1, 0.15, 0.2, 0.3, 0.25]  # Observaciones en el tiempo
transition_noise = 0.05  # Ruido en la transición del estado
observation_noise = 0.1  # Ruido en las observaciones

# Ejecutar el filtro de partículas
for observation in observations:
    estimated_state = particle_filter(num_particles, initial_state, [observation], transition_noise, observation_noise)
    true_state.append(estimated_state)

print("Verdadero estado:", true_state)
