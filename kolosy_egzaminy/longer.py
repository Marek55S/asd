# zadanie offline z 21/22
# Dany jest graf nieskierowany G = (V, E) oraz dwa wierzchołki s, t ∈ V . Proszę zaproponować i
# zaimplementować algorytm, który sprawdza, czy istnieje taka krawędź {p, q} ∈ E, której usunięcie
# z E spowoduje wydłużenie najkrótszej ścieżki między s a t (usuwamy tylko jedną krawędź). Algo-
# rytm powinien być jak najszybszy i używać jak najmniej pamięci. Proszę skrótowo uzasadnić jego
# poprawność i oszacować złożoność obliczeniową.
# Algorytm należy zaimplementować jako funkcję:
# def longer(G, s, t):
# która przyjmuje graf G oraz numery wierzchołków s, t i zwraca dowolną krawędź spełniającą
# warunki zadania, lub None jeśli takiej krawędzi w G nie ma. Graf przekazywany jest jako lista list
# sąsiadów, t.j. G[i] to lista sąsiadów wierzchołka o numerze i. Wierzchołki numerowane są od 0.
# Funkcja powinna zwrócić krotkę zawierającą numery dwóch wierzchołków pomiędzy którymi jest
# krawędź spełniająca warunki zadania, lub None jeśli takiej krawędzi nie ma. Jeśli w grafie oryginalnie
# nie było ścieżki z s do t to funkcja powinna zwrócić None.

# podstawowa zlozonosc - na mniej punktow
from collections import deque


def bfs(graph, start, end):
    n = len(graph)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [float("inf") for _ in range(n)]
    queue = deque()
    queue.append(start)
    distance[start] = 0
    visited[start] = True
    while queue:
        curr = queue.popleft()
        for ngh in graph[curr]:
            if not visited[ngh]:
                visited[ngh] = True
                parent[ngh] = curr
                distance[ngh] = distance[curr] + 1
                queue.append(ngh)
                """if ngh == end:
                    return distance[ngh], parent"""
    if distance[end] is not None:
        return distance[end], parent
    else:
        return None


def bfs_del_edg(graph, start, end, edge):
    n = len(graph)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [float("inf") for _ in range(n)]
    queue = deque()
    queue.append(start)
    distance[start] = 0
    visited[start] = True
    ver1, ver2 = edge
    while queue:
        curr = queue.popleft()
        for ngh in graph[curr]:
            if min(curr, ngh) != min(ver1, ver2) or max(curr, ngh) != max(ver1, ver2):
                if not visited[ngh]:
                    visited[ngh] = True
                    parent[ngh] = curr
                    distance[ngh] = distance[curr] + 1
                    queue.append(ngh)
                    if ngh == end:
                        return distance[ngh]
    return None


def longer(G, s, t):

    shortest, parent = bfs(G, s, t)
    spath = []
    if shortest is None:
        return None

    def findpath(ver):
        nonlocal parent, spath
        if parent[ver] is not None:
            spath.append((parent[ver], ver))
            findpath(parent[ver])

    findpath(t)
    for edge in spath:
        new_dist = bfs_del_edg(G, s, t, edge)
        if new_dist is None or new_dist > shortest:
            return edge
    return None


G = [
    [1, 2],  # 0
    [0, 3],  # 1
    [0, 4],  # 2
    [1, 5, 6],  # 3
    [2, 7],  # 4
    [3, 8],  # 5
    [3, 8],  # 6
    [4, 8],  # 7
    [5, 6, 7, 9],  # 8
    [8, 10, 11],  # 9
    [9, 12],  # 10
    [9, 12],  # 11
    [10, 11],
]  # 12
# print(longer(G, 0, 12))
# print(bfs_del_edg(G, 0, 12, (8, 9)))


# lepsza zlozonosc - na wiecej punktow
# nie dziala - zle zrobione
def bfs_2(graph, start):
    n = len(graph)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    queue = deque()
    visited[start] = True
    queue.append(start)
    while queue:
        curr = queue.popleft()
        for ngh in graph[curr]:
            if not visited[ngh]:
                visited[ngh] = True
                parent[ngh] = curr
                queue.append(ngh)
    return parent


def make_graph(edges, nver):
    n = len(edges)
    newgraph = [[] for _ in range(nver)]
    for u, v in edges:
        newgraph[u].append(v)
        newgraph[v].append(u)
    return newgraph


def find_bridge(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    time = [None for _ in range(n)]
    parent = [None for _ in range(n)]
    low = [None for _ in range(n)]
    ctime = 0
    time[0] = ctime
    low[0] = ctime

    def dfs(curr):
        nonlocal ctime, graph, visited, parent, low, time
        visited[curr] = True
        ctime += 1
        time[curr] = ctime
        low[curr] = ctime
        for neighbour in graph[curr]:
            if not visited[neighbour]:
                parent[neighbour] = curr
                dfs(neighbour)
                low[curr] = min(low[curr], low[neighbour])
                if low[neighbour] > time[curr]:
                    return (curr, neighbour)
            elif neighbour != parent[curr]:
                low[curr] = min(low[curr], time[neighbour])

    for v in range(n):
        if not visited[v]:
            dfs(v)
    return None


def longer_better(G, s, t):
    n = len(G)
    sparent = bfs_2(G, s)
    tparent = bfs_2(G, t)
    edg = set()

    def findpath(par, curr):
        nonlocal edg
        if par[curr] is not None:
            if (min(par[curr], curr), max(par[curr], curr)) not in edg:
                edg.add((min(par[curr], curr), max(par[curr], curr)))
            findpath(par, par[curr])

    findpath(sparent, t)
    findpath(tparent, s)
    newgraph = make_graph(edg, n)
    return find_bridge(newgraph)


# print(longer_better(G, 0, 12))
G1 = [[1, 2], [0, 2], [0, 1]]
print(longer_better(G, 0, 12))
