# algorytm bellmana-forda dla listy sasiedztwa
# dziala ten dla listy krawedzi, ale dla listy sasiedztwa nie radzi sobie z wagami ujemnymi


# trzeba naprawic mozliwosc przejscia 2 razy przez krawedz dla wagi ujemnej w grafie nieskierowanym
def bford(graph, start, end):
    n = len(graph)
    time = [float("inf") for _ in range(n)]
    parent = [None for _ in range(n)]
    time[start] = 0

    # w funkcji relax u jest pierwszym wierzcholkiem, v jest drugim, a w jest waga krawedzi miedzy nimi
    def relax(u, v, w):
        nonlocal time, parent
        if time[v] > time[u] + w:
            time[v] = time[u] + w
            # parent[v] = (w, u)
            parent[v] = (u, w)

    for _ in range(n - 1):
        for u in range(n):
            for w, v in graph[u]:
                relax(u, v, w)

    for u in range(n):
        for v, w in graph[u]:
            if time[v] > time[u] + w:
                return False
    return time

    """for ver in range(n):
        for etm, neighbour in graph[ver]:
            relax(ver, neighbour, etm)
    print(time, parent)"""

    """for u in range(n):
        for w, v in graph[u]:
            if time[v] > time[u] + w:
                return False
    return time[end]"""


Gind = [
    [(4, 2)],
    [(3, 2), (2, 4)],
    [(4, 0), (3, 1), (1, 3)],
    [(1, 2), (3, 4)],
    [(2, 1), (1, 5), (2, 6)],
    [(1, 4), (-5, 6)],
    [(2, 4), (-5, 5)],
]

Gdir = [[(4, 2)], [(2, 4)], [(3, 1), (1, 3)], [(3, 4)], [(2, 6)], [(1, 4)], [(-2, 5)]]

# print(bford(Gdir, 0, 6))


# bellman ford dla grafu reprezentowanego listą krawędzi
# graf:(wierzcholek startowy,wierzcholek koncowy, waga)
def bellman_ford_edges(graph, start):
    n = max(max(u, v) for u, v, w in graph) + 1
    time = [float("inf") for _ in range(n)]
    parent = [None for _ in range(n)]
    time[start] = 0

    def relax(u, v, w):
        nonlocal time, parent
        if time[v] > time[u] + w:
            time[v] = time[u] + w
            parent[v] = u

    for _ in range(n - 1):
        for u, v, w in graph:
            relax(u, v, w)

    for u, v, w in graph:
        if time[v] > time[u] + w:
            return False
    return time


edges_dir = [
    (0, 2, 4),
    (1, 4, 2),
    (2, 1, 3),
    (2, 3, 1),
    (3, 4, 3),
    (4, 6, 2),
    (5, 4, 1),
    (6, 5, -3),
]
print(bellman_ford_edges(edges_dir, 0))
