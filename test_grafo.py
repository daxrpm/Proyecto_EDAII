import pytest
from grafo import Grafo


@pytest.fixture
def grafo_ejemplo():

    grafo = Grafo()

    # Agregar nodos
    for nodo in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        grafo.agregar_nodo(nodo)

    # Agregar aristas dirigidas
    grafo.agregar_arista('A', 'B')
    grafo.agregar_arista('A', 'C')
    grafo.agregar_arista('B', 'D')
    grafo.agregar_arista('B', 'E')
    grafo.agregar_arista('C', 'F')
    grafo.agregar_arista('D', 'G')
    grafo.agregar_arista('E', 'G')
    grafo.agregar_arista('F', 'G')

    return grafo


class TestBfsCamino:

    def test_camino_existe(self, grafo_ejemplo):
        camino = grafo_ejemplo.bfs_camino('A', 'G')
        assert camino is not None
        assert camino[0] == 'A'
        assert camino[-1] == 'G'
        assert len(camino) > 1

    def test_mismo_nodo(self, grafo_ejemplo):
        camino = grafo_ejemplo.bfs_camino('A', 'A')
        assert camino == ['A']

    def test_sin_camino(self, grafo_ejemplo):
        # Agregar nodo aislado
        grafo_ejemplo.agregar_nodo('H')
        camino = grafo_ejemplo.bfs_camino('A', 'H')
        assert camino is None

    def test_nodos_inexistentes(self, grafo_ejemplo):
        camino = grafo_ejemplo.bfs_camino('X', 'Y')
        assert camino is None


class TestBfsArbol:

    def test_arbol_completo(self, grafo_ejemplo):
        arbol = grafo_ejemplo.bfs_arbol('A')

        assert 'A' in arbol
        assert len(arbol) > 0

        # Verificar que A tiene hijos
        assert len(arbol['A']) > 0

    def test_arbol_nodo_aislado(self, grafo_ejemplo):
        grafo_ejemplo.agregar_nodo('H')
        arbol = grafo_ejemplo.bfs_arbol('H')

        assert 'H' in arbol
        assert arbol['H'] == []

    def test_arbol_nodo_inexistente(self, grafo_ejemplo):
        arbol = grafo_ejemplo.bfs_arbol('X')
        assert arbol == {}


class TestDfsCamino:

    def test_camino_existe(self, grafo_ejemplo):
        camino = grafo_ejemplo.dfs_camino('A', 'G')
        assert camino is not None
        assert camino[0] == 'A'
        assert camino[-1] == 'G'
        assert len(camino) > 1

    def test_mismo_nodo(self, grafo_ejemplo):
        camino = grafo_ejemplo.dfs_camino('A', 'A')
        assert camino == ['A']

    def test_sin_camino(self, grafo_ejemplo):
        grafo_ejemplo.agregar_nodo('H')
        camino = grafo_ejemplo.dfs_camino('A', 'H')
        assert camino is None

    def test_nodos_inexistentes(self, grafo_ejemplo):
        camino = grafo_ejemplo.dfs_camino('X', 'Y')
        assert camino is None


class TestDfsArbol:

    def test_arbol_completo(self, grafo_ejemplo):
        arbol = grafo_ejemplo.dfs_arbol('A')

        assert 'A' in arbol
        assert len(arbol) > 0

        # Verificar que A tiene hijos
        assert len(arbol['A']) > 0

    def test_arbol_nodo_aislado(self, grafo_ejemplo):
        grafo_ejemplo.agregar_nodo('H')
        arbol = grafo_ejemplo.dfs_arbol('H')

        assert 'H' in arbol
        assert arbol['H'] == []

    def test_arbol_nodo_inexistente(self, grafo_ejemplo):
        arbol = grafo_ejemplo.dfs_arbol('X')
        assert arbol == {}


class TestComparacionBfsDfs:

    def test_ambos_encuentran_camino(self, grafo_ejemplo):
        camino_bfs = grafo_ejemplo.bfs_camino('A', 'G')
        camino_dfs = grafo_ejemplo.dfs_camino('A', 'G')

        assert camino_bfs is not None
        assert camino_dfs is not None
        assert camino_bfs[0] == camino_dfs[0] == 'A'
        assert camino_bfs[-1] == camino_dfs[-1] == 'G'

    # TODO: Analize Big O complexity for BFS and DFS
    # def test_bfs_encuentra_camino_mas_corto(self, grafo_ejemplo):
    #     # BFS siempre encuentra el camino más corto
    #     camino_bfs = grafo_ejemplo.bfs_camino('A', 'G')
    #     camino_dfs = grafo_ejemplo.dfs_camino('A', 'G')

    #     assert len(camino_bfs) <= len(camino_dfs)
