# Marek Swakoń
# heurystyka testy probne 11/13 w 0.01, testy główne 2/13
"""Mój algorytm na początku wywołuje funkcję matrix_tolist, która zamienia macierz incydencji
    na postać listy sąsiedztwa. Następnie wywoływana jest funkcja djikstra, która wykonuje algorytm djikstry
    oraz zwraca najkrótszą ścieżkę w postaci listy kolejno odwiedzanych wierzchołków.
    Potem, funkcja wpisuje do tablic weight i minimal, odpowiednio wagi krawędzi między wierzchołkami najkrótszej
    ścieżki oraz mniejszą z wartości sąsiednich krawędzi. Kolejna pętla przechodzi po tablicy minimal
    i po kolei wyznacza krawędzie po których najlepiej będzie przeskoczyć dwumilowymi butami.
    Na końcu, do zmiennej sum wpisywana jest suma wag krawędzi z najkrótszej ścieżki oraz odejmowane są wagi
    krawędzi po których przeskakujemy"""
from zad6testy import runtests
from queue import PriorityQueue


def matrix_tolist(graph):
    n = len(graph)
    nlist = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                nlist[i].append((graph[i][j], j))
    return nlist


def djikstra(graph, start, end):
    n = len(graph)
    distance = [float("inf") for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = PriorityQueue()
    Q.put((0, start))
    distance[start] = 0
    while not Q.empty():
        ver = Q.get()[1]
        for w, v in graph[ver]:
            if distance[v] > distance[ver] + w:
                distance[v] = distance[ver] + w
                parent[v] = ver
                Q.put((w, v))
            if v == end:
                break
    path = []

    def findpath(ver):
        nonlocal parent, path, start
        path.append(ver)
        if ver == start:
            return
        return findpath(parent[ver])

    findpath(end)
    path.reverse()
    return path


def jumper(G, s, w):
    glist = matrix_tolist(G)
    path = djikstra(glist, s, w)
    minimal = [0 for _ in range(len(G) + 2)]
    weight = [0 for _ in range(len(G) - 1)]
    to_jump = [False for _ in range(len(minimal))]
    for i in range(1, len(path)):
        weight[i - 1] = G[path[i - 1]][path[i]]
    for i in range(1, len(weight)):
        minimal[i + 1] = min(weight[i - 1], weight[i])
    for i in range(2, len(minimal) - 1):
        high = 0
        hidx = None
        for j in range(2, len(minimal)):
            print(j)
            if (
                minimal[j] > high
                and not to_jump[j]
                and not to_jump[j - 2]
                and not to_jump[j - 1]
                and not to_jump[j + 1]
                and not to_jump[j + 2]
            ):
                high = minimal[j]
                hidx = j
        # print(high)
        if hidx is None:
            break
        to_jump[hidx] = True
    sum = 0
    for w in weight:
        sum += w
    for i in range(2, len(to_jump) - 2):
        if to_jump[i]:
            sum -= minimal[i]
    return sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(jumper, all_tests=True)
