# Marek Swakoń
# Mój algorytm na początku wywołuje funkcję to_graph, ktora przeksztalca
# mape do grafu w postaci listy sasiedztwa.Kazde pole traktowane jest jako wierzcholek,
# a krawedzie sa tworzone tylko miedzy sasiadujacymi polami, z pola o mniejszej wartosci
# do pola o wiekszej wartosci. W funkcji trip, po przygotowaniu grafu, tworzone sa tablice
# visited oraz result, ktore przechowuja odpowiednio stan odwiedzenia wierzcholka, oraz
# najdluzsza sciezke rozpoczynajaca sie w danym wierzcholku.
# Dla kazdego nieodwiedzonego wierzcholka wywolywana jest funkcja dfs, ktora
# realizuje standardowy algorytm dfs, ale po przejsciu kazdej krawedzi jest
# aktualizowana dlugosc maksymalnej sciezki, na maksimum z : najdluzszej policzonej do
# tej pory sciezki aktualnie przegladanego wierzcholka, oraz powiekszonej o 1 najdluzszej
# sciezki zaczynajacej sie w aktualnie rozwazanym sasiadzie.
# Na koncu funkcja trip zwraca maksymalna wartosc z tablicy result
# zlozonosc czasowa tego algorytmu wynosi O(mn), a zlozonosc pamieciowa O(mn)

from zad9testy import runtests


def to_graph(map):
    m = len(map)
    n = len(map[0])
    new_graph = [[] for _ in range(m * n)]

    def add_edge(u, v):
        u_ind = u[0] * n + u[1]
        v_ind = v[0] * n + v[1]
        if map[u[0]][u[1]] < map[v[0]][v[1]]:
            new_graph[u_ind].append(v_ind)

    for i in range(m):
        for j in range(n):
            if i > 0:
                add_edge((i, j), (i - 1, j))
            if i < m - 1:
                add_edge((i, j), (i + 1, j))
            if j > 0:
                add_edge((i, j), (i, j - 1))
            if j < n - 1:
                add_edge((i, j), (i, j + 1))

    return new_graph


def trip(M):
    graph = to_graph(M)
    mn = len(graph)
    visited = [False for _ in range(mn)]
    result = [1 for _ in range(mn)]

    def dfs(curr):
        nonlocal visited, result, graph
        visited[curr] = True
        for ngh in graph[curr]:
            if not visited[ngh]:
                dfs(ngh)
            result[curr] = max(result[curr], result[ngh] + 1)

    for i in range(mn):
        if not visited[i]:
            dfs(i)
    return max(result)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(trip, all_tests=True)
