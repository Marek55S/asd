# algorytm floyda warshalla dla grafu w reprezentacji listy sąsiedztwa


def f_warshall(graph):
    n = len(graph)
    dist = [[float("inf") for _ in range(n)] for _ in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]
    # przeksztalcenie na macierz
    for ver in range(n):
        dist[ver][ver] = 0
        for w, neighbour in graph[ver]:
            dist[ver][neighbour] = w
            parent[ver][neighbour] = ver
    for u in range(n):
        for v1 in range(n):
            for v2 in range(n):
                if dist[v1][v2] > dist[v1][u] + dist[u][v2]:
                    dist[v1][v2] = dist[v1][u] + dist[u][v2]
                    parent[v1][v2] = parent[u][v2]
    return dist


G = [
    [(5, 1), (4, 2), (8, 3)],
    [(-4, 0), (-2, 2), (5, 4)],
    [(5, 3), (2, 4)],
    [(-1, 0), (2, 1), (-1, 4)],
    [(4, 2), (2, 3)],
]

time = f_warshall(G)
for i in range(len(time)):
    for j in range(len(time)):
        print("d[", i, ",", j, "]", " = ", time[i][j])
