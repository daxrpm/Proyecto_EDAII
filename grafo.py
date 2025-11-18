from nodo import Nodo
class Grafo:

    #Constrcutor Grafo 

    def __init__(self):
        self.nodos = {}
        self.aristas = []

    # Agregar nodo al grafo
    def agregar_nodo(self, nombre_nodo):
        if nombre_nodo not in self.nodos:
            nuevo_nodo = Nodo(nombre_nodo)
            self.nodos[nombre_nodo] = nuevo_nodo





    # Agregar arista al grafo
    #def agregar_arista(self, nodo_origen, nodo_destino, peso=1):

    