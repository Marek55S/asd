# mosty w grafie nieskierowany


def mosty_ind(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    time = [None for _ in range(n)]
    parent = [None for _ in range(n)]
    low = [None for _ in range(n)]
    mosty = set()
    ctime = 0
    time[0] = ctime
    low[0] = ctime

    def dfs(curr):
        nonlocal ctime, graph, visited, parent, low, time, mosty
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
                    # print(f"Most: {curr} - {neighbour}")
                    mosty.add((curr, neighbour))
            elif neighbour != parent[curr]:
                low[curr] = min(low[curr], time[neighbour])

    for v in range(n):
        if not visited[v]:
            dfs(v)
    return mosty


G = [
    [1, 4],
    [0, 2],
    [1, 3],
    [2, 4, 5],
    [0, 3],
    [3, 6, 9],
    [5, 7],
    [6, 8],
    [7, 9],
    [8, 5],
]

# print(mosty_ind(G))

# most w grafie skierowanym


def mosty_dir(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    time = [None for _ in range(n)]
    parent = [None for _ in range(n)]
    low = [None for _ in range(n)]
    mosty = set()
    ctime = 0
    time[0] = ctime
    low[0] = ctime

    def dfs(curr, prev):
        nonlocal ctime, graph, visited, parent, low, time, mosty
        visited[curr] = True
        ctime += 1
        time[curr] = ctime
        low[curr] = ctime
        for neighbour in graph[curr]:
            if not visited[neighbour]:
                parent[neighbour] = curr
                dfs(neighbour, curr)
                low[curr] = min(low[curr], low[neighbour])
                if low[neighbour] > time[curr]:
                    mosty.add((curr, neighbour))
            # elif neighbour != parent[curr]:
            else:
                low[curr] = min(low[curr], time[neighbour])

    for v in range(n):
        if not visited[v]:
            dfs(v, None)
    return mosty


G2 = [[1], [4], [0, 3], [], [2, 5], [6], [7], [5]]
print(mosty_dir(G2))
