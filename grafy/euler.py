# znajdowanie cyklu eulera w grafie
# chyba dziala ale idk


def ecycle(graph):
    visited = [False for _ in range(len(graph))]
    cycle = []

    def rek(curr):
        nonlocal graph, cycle
        # petla przechodzi przez krawedzi wychodzace z wierzcholka curr i po przejsciu usuwa je z grafu
        while graph[curr]:
            neighbour = graph[curr].pop()
            rek(neighbour)
        visited[curr] = True
        # dodaje do cyklu wierzcholek po przejsciu wszystkich jego krawedzi
        cycle.append(curr)

    rek(0)
    return cycle


G = [
    [1, 2],
    [0, 2, 3, 4, 5, 6],
    [0, 1, 3, 5, 6],
    [1, 2, 4, 5],
    [1, 3, 5],
    [1, 2, 3, 4],
    [1, 2],
]

print(ecycle(G))
