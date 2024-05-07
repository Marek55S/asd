# sortowanie topologiczne w reprezentacji grafu listy sasiedztwa
# mozliwe tylko w grafie acyklicznym skierowanym


def topologic_sort(graph, start):
    visited = [False for _ in range(len(graph))]
    sorted = []

    # zwykly dfs tylko po przetworzeniu wierzcholka jest on wpisywany na poczatek posortowanej listy
    def rek(curr_v):
        nonlocal graph, sorted
        visited[curr_v] = True
        for v in graph[curr_v]:
            if not visited[v]:
                rek(v)
        # tu wierzcholek curr_v zostal przetworzony i wpisujemy go do listy
        sorted = [curr_v] + sorted

    rek(start)
    return sorted


G = [[0, 1, 2], [1, 2, 4], [2], [3], [4, 3, 5, 6], [5], [6]]
print(topologic_sort(G, 0))
