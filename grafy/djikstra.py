from queue import PriorityQueue


def adj_list(edges, n):
    graph = [[] for _ in range(n + 1)]
    for u, v, dist in edges:
        graph[u].append((dist, v))
        graph[v].append((dist, u))
    return graph


def djikstra(G, s, e):
    n = len(G)
    parent = [None for _ in range(n)]
    distance = [float("inf") for _ in range(n)]
    Q = PriorityQueue()
    distance[s] = 0
    Q.put((0, s))
    while not Q.empty():
        u = Q.get()[1]
        for w, v in G[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                parent[v] = u
                Q.put((distance[v], v))
            if u == e:
                return distance[u]
    return distance, parent


E = [
    (0, 1, 5),
    (1, 2, 21),
    (1, 3, 1),
    (2, 4, 7),
    (3, 4, 13),
    (3, 5, 16),
    (4, 6, 4),
    (5, 6, 1),
]
Gr = adj_list(E, 6)
# print(Gr)
print(djikstra(Gr, 1, 5))
