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

    # Agregar arista dirigida de nodo1 a nodo2
    def agregar_arista(self, nodo1, nodo2):
        if nodo1 in self.nodos and nodo2 in self.nodos:
            self.nodos[nodo1].agregar_vecino(nodo2)

    # BFS para encontrar camino de un nodo inicio a un nodo destino
    def bfs_camino(self, inicio, destino):

        if inicio not in self.nodos or destino not in self.nodos:
            return None

        if inicio == destino:
            return [inicio]

        # Cola para BFS: (nodo_actual, camino_hasta_aqui)
        cola = [(inicio, [inicio])]
        visitados = {inicio}

        while cola:
            nodo_actual, camino = cola.pop(0)

            # Explorar vecinos
            for vecino in self.nodos[nodo_actual].vecinos:
                if vecino == destino:
                    return camino + [vecino]

                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, camino + [vecino]))

        return None  # No hay camino

    # BFS para obtener el árbol BFS desde un nodo inicio
    def bfs_arbol(self, inicio):
        if inicio not in self.nodos:
            return {}

        # Árbol BFS: {nodo: [hijos]}
        arbol = {inicio: []}
        # Diccionario para rastrear padres (para construir el árbol)
        padres = {inicio: None}
        # Cola para BFS
        cola = [inicio]
        visitados = {inicio}

        while cola:
            nodo_actual = cola.pop(0)

            # Inicializar lista de hijos si no existe
            if nodo_actual not in arbol:
                arbol[nodo_actual] = []

            # Explorar vecinos
            for vecino in self.nodos[nodo_actual].vecinos:
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = nodo_actual
                    cola.append(vecino)

                    # Agregar vecino como hijo del nodo actual en el árbol
                    arbol[nodo_actual].append(vecino)
                    # Inicializar lista de hijos para el vecino
                    arbol[vecino] = []

        return arbol
