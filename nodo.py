class Nodo:

    # Constructor del Nodo 
    def __init__(self, nombre):
        self.nombre = nombre 
        self.vecinos = []

    # Agregar vecino al nodo
    def agregar_vecino(self, nombre_vecino):
        if nombre_vecino not in self.vecinos:
            self.vecinos.append(nombre_vecino)