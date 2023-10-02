import numpy as np


class NeuronaArtificial:
    def __init__(self, num_entradas):
        # Inicializamos los pesos y el sesgo de manera aleatoria
        self.pesos = np.random.rand(num_entradas)
        self.sesgo = np.random.rand()

    def activacion(self, entradas):
        # Realizamos el producto escalar de las entradas y los pesos, y le sumamos el sesgo
        suma_ponderada = np.dot(entradas, self.pesos) + self.sesgo
        # Aplicamos una función de activación (por ejemplo, sigmoide)
        activacion = 1 / (1 + np.exp(-suma_ponderada))
        return activacion


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una neurona con 3 entradas
    neurona = NeuronaArtificial(3)

    # Entradas de ejemplo
    entradas = np.array([0.5, 0.3, 0.8])

    # Calcular la salida de la neurona
    salida = neurona.activacion(entradas)

    # Imprimir la salida
    print("Salida de la neurona:", salida)