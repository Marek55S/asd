# Marek Swakon
# nie dziala, testy 3/14
# moj algorytm tworzy graf o n^2 wierzcholkach, gdzie mozliwe opcje przejscia to krawedzie,
# a komnaty to wierzcholki. Nastepnie wykonuje algorytm dfs rekurencyjnie i zwraca czas dotarcia
# do ostatniego wierzcholka
# zlozonosc czasowa to (n^2)*(logn), a zlozonosc pamieciowa to n^2
from zad7testy import runtests


def spacecheck(row, col, n):

    if row < 0 or row >= n:
        return False
    if col < 0 or col >= n:
        return False
    return True


def makegraph(array):
    n = len(array)
    newgraph = [[] for _ in range(n * n)]
    for i in range(n):
        for j in range(n):
            if array[i][j] == ".":
                if spacecheck(i + 1, j, n) and array[i + 1][j] == ".":
                    newgraph[(i + 1) * n + j].append(i * n + j)
                    newgraph[i * n + j].append((i + 1) * n + j)
                if spacecheck(i, j + 1, n) and array[i][j + 1] == ".":
                    newgraph[i * n + j].append(i * n + j + 1)
    return newgraph


def dfs(graph, start):
    n = len(graph)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    time = [0 for _ in range(n)]

    def rek(curr_v):
        nonlocal graph
        visited[curr_v] = True
        for v in graph[curr_v]:
            if not visited[v]:
                parent[v] = curr_v
                time[v] = time[curr_v] + 1
                rek(v)

    rek(start)
    return time


def maze(L):
    G = makegraph(L)
    n = len(G)
    time = dfs(G, 0)
    return time[n - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
