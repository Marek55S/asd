# dfs dla listy
def DFS(graph, start):
    visited = [False for _ in range(len(graph))]
    parent = [None for _ in range(len(graph))]

    def rek(curr_v):
        nonlocal graph
        visited[curr_v] = True
        for v in graph[curr_v]:
            if not visited[v]:
                parent[v] = curr_v
                rek(v)

    rek(start)


G = [[1, 2], [0, 3], [0, 3, 5], [1, 2, 4, 5], [3, 6], [2, 3, 6], [4, 5]]
DFS(G, 0)
