import csv


def cargar_nodos(ruta_archivo):
    nodos = {}
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            id_nodo = fila['Id']
            label = fila['Label']
            nodos[id_nodo] = label
    return nodos


def cargar_aristas(ruta_archivo):
    aristas = []
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            source = fila['Source']
            target = fila['Target']
            if source and target:
                aristas.append((source, target))
    return aristas
