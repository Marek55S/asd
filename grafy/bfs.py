from collections import deque
from reprezentacje import matrix_undir, adj_list_undir


# dla grafu nieskierowanego reprezentowanego macierza
def bfs_matrix(graph, start):
    visited = [False] * len(graph)
    queue = deque()
    queue.append(start)
    visited[start] = True
    n = len(graph)

    while queue:
        curr_vertex = queue.popleft()
        print(curr_vertex)
        for neighbour in range(n):
            if graph[curr_vertex][neighbour] == True and visited[neighbour] == False:
                queue.append(neighbour)
                visited[neighbour] = True


# graph- graf w reprezentacji listy sasiedztwa, start - wierzcholek startowy
def bfs_adjlist(graph, start):
    visited = [False] * len(graph)
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        curr_vertex = queue.popleft()
        print(curr_vertex)
        for neighbour in graph[curr_vertex]:
            if visited[neighbour] is False:
                queue.append(neighbour)
                visited[neighbour] = True


edges = [(0, 1), (0, 2), (2, 3), (1, 4), (3, 4), (2, 5), (5, 6), (6, 7)]

bfs_adjlist(adj_list_undir(edges, 8), 0)
print(adj_list_undir(edges, 8))
