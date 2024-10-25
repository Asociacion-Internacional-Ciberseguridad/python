from queue import PriorityQueue

def a_star(inicio, meta, grafo, heuristica):
    cola = PriorityQueue()
    cola.put((0, inicio))
    costos = {inicio: 0}
    came_from = {inicio: None}

    while not cola.empty():
        _, actual = cola.get()

        if actual == meta:
            return reconstruir_camino(came_from, actual)

        for vecino in grafo[actual]:
            nuevo_costo = costos[actual] + grafo[actual][vecino]
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica[vecino]
                cola.put((prioridad, vecino))
                came_from[vecino] = actual

def reconstruir_camino(came_from, actual):
    camino = []
    while actual is not None:
        camino.append(actual)
        actual = came_from[actual]
    return camino[::-1]

grafo = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1},
    'C': {'D': 1},
    'D': {}
}
heuristica = {'A': 4, 'B': 2, 'C': 2, 'D': 0}

print(a_star('A', 'D', grafo, heuristica))
