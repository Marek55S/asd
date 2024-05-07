# dostaje tablice krotek ktore reprezentuja krawedzie grafu nieskierowanego i tworzy macierz reprezentujaca ten graf
def matrix_undir(E, n):
    graph = [[False for _ in range(n)] for _ in range(n)]
    for i in E:
        v1, v2 = i
        graph[v1][v2] = True
        graph[v2][v1] = True
    return graph


# analogiczny jak wyżej ale tworzy macierz dla grafu skierowanego
def matrix_dir(E, n):
    graph = [[False for _ in range(n)] for _ in range(n)]
    for i in E:
        v1, v2 = i
        graph[v1][v2] = True
    return graph


# tworzy liste sasiedztwa dla grafu, ktorego lista kraawedzi jest przekazywana do funkcji
def adj_list_undir(E, n):
    graph = [[i] for i in range(n)]
    for j in E:
        v1, v2 = j
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph


# analogicznie jak wyzej ale tworzy graf skierowany
def adj_list_dir(E, n):
    graph = [[i] for i in range(n)]
    for j in E:
        v1, v2 = j
        graph[v1].append(v2)
    return graph


edges = [(1, 2), (0, 1), (0, 2)]
