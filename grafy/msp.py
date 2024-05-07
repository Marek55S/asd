# minimalne drzewa spinajace, algorytmy kruskala i prima
# algorytmy dla grafow nieskierowanych

# algorytm kruskala
# dla grafu w postaci listy krawedzi
# (waga, wierzcholek1, wierzcholek2)


# dziala
def partition(array, l, r):
    pivot = array[r][0]
    i = l - 1
    for j in range(l, r):
        if array[j][0] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[r], array[i + 1] = array[i + 1], array[r]
    return i + 1


def quicksort(array, l, r):
    if l < r:
        pivot_idx = partition(array, l, r)
        quicksort(array, l, pivot_idx - 1)
        quicksort(array, pivot_idx + 1, r)


def kruskal(graph):
    # sortowanie krawedzi niemalejaco wedlug wagi
    quicksort(graph, 0, len(graph) - 1)
    maxv = max(max(graph[i][1], graph[i][2]) for i in range(len(graph)))
    parent = [i for i in range(maxv + 1)]
    rank = [0 for _ in range(maxv + 1)]
    minimaltree = set()

    # znajdowanie korzenia dla drzewa do ktorego nalezy wierzcholek ver
    def root(ver):
        nonlocal parent
        if parent[ver] == ver:
            return ver
        return root(parent[ver])

    # funkcja laczy drzewa do ktorych naleza wierzcholki u i v  w jedno drzewo
    def union(u, v):
        nonlocal parent, rank
        u_root = root(u)
        v_root = root(v)
        if rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        elif rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1

    # petla sprawdza wszystkie krawedzie grafu i dodaje odpowiednie do minimalnego drzewa
    for edge in graph:
        w, u, v = edge
        if root(u) != root(v):
            minimaltree.add(edge)
            union(u, v)
    return minimaltree


G = [(1, 0, 4), (3, 0, 1), (4, 1, 4), (5, 1, 2), (6, 2, 4), (2, 2, 3), (7, 3, 4)]
print(kruskal(G))


# argorytm prima
# dla grafu w reprezentcji listy sąsiedztwa

from queue import PriorityQueue


# zamiana z listy krawędzie na liste sąsiedztwa
def adj_list(edges):
    n = max(max(edges[i][1], edges[i][2]) for i in range(len(edges)))
    graph = [[] for _ in range(n + 1)]
    for dist, u, v in edges:
        graph[u].append((dist, v))
        graph[v].append((dist, u))
    return graph


def prim(graph):
    visited = [False for _ in range(len(graph))]
    parent = [None for _ in range(len(graph))]
    minimaltree = set()
    sum = 0
    Q = PriorityQueue()
    visited[0] = True
    for w, v in graph[0]:
        Q.put((w, 0, v))

    while not all(visited):
        distance, source, ver = Q.get()
        if not visited[ver]:
            minimaltree.add((distance, source, ver))
            visited[ver] = True
            sum += distance
            for w, neighbour in graph[ver]:
                if not visited[neighbour]:
                    Q.put((w, ver, neighbour))
                    parent[neighbour] = ver

    return minimaltree


G2 = adj_list(G)
print(prim(G2))
