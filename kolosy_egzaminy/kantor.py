# mamy kantor, mamy macierz zawierajaca kursy za pomoca innej waluty
# mamy znalezc takie przewalutowania, zeby zarobic czyli wplacona na poczatku suma
# ma byc mniejsza od wyplaconej ( jest to graf skierowany wazony)


def kantor(graph, start):
    n = len(graph)
    costs = [float("-inf") for _ in range(n)]
    parent = [None for _ in range(n)]
    costs[start] = 1
    path = []

    for _ in range(n - 1):
        for v in range(n):
            for u, val in graph[v]:
                value = costs[v] / val
                if costs[u] < value:
                    costs[u] = value
                    parent[u] = v
    if costs[start] > 1:
        path.append(start)
        current = start

        while len(path) <= 1 or current != start:
            current = parent[current]
            path.append(current)
    path.reverse()
    print(path)
    return costs


G = [[(1, 0.98)], [(2, 0.98)], [(0, 0.98)]]
print(kantor(G, 0))
