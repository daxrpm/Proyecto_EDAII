from nodo import Nodo


class Grafo:

    # Constrcutor Grafo

    def __init__(self):
        self.nodos = {}

    # Agregar nodo al grafo
    def agregar_nodo(self, nombre_nodo):
        if nombre_nodo not in self.nodos:
            nuevo_nodo = Nodo(nombre_nodo)
            self.nodos[nombre_nodo] = nuevo_nodo
