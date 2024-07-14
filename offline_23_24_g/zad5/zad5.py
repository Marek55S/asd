# Marek Swakoń
# testy 10/10 czas 0.12s
"""Moj algorytm na poczatku tworzy graf w reprezentacji listy sasiedztwa, a nastepnie wywoluje funkcje djikstra,
   ktora jest zmodyfikowanym algorytmem djikstry.Funkcja ta tworzy tablice distance przechowujaca
   czas dotarcia do planety(wierzcholka),inicjuje kolejke priorytetowa oraz wpisuje czas 0 dla planety poczatkowej
   i dodaje ja do kolejki. W dalszej czesci wywolywana jest petla while dzialajaca dopuki kolejka nie jest pusta.
   z kolejki Q wyciagany jest wierzcholek ktory bedziemy rozpatrywac. Sprawdzam, czy ten wierzcholek znajduje sie
   w tablicy anomalii czasowych, jezeli tak, to dodaje wszystkie wierzcholki z tej tablicy do kolejki, nie 
   zwiekszajac czasu, oraz sprawdzam, czy zaden z nich nie jest wierzcholkiem koncowym. Po sprawdzeniu anomalii,
   wywolywana jest petla for sprawdzajaca, czy znaleziona sciezka, jest krotsza niz ta zapisana w tablicy distance.
   Jezeli tak jest, to wartosc w tablicy jest aktualizowana, a sprawdzony w ten sposob wierzcholek jest dodawany
   do kolejki z nowym czasem dotarcia. Po zakonczeniu funkcji while, funkcja sprawdza czy wierzcholek udalo
   sie osiagnac, jezeli nie, to zwraca None, a w przeciwnym wypadku zwraca obliczony czas dotarcia.
   Zlozonosc czasowa algorytmu to O(V^2), a pamieciowa to O(V)"""
from zad5testy import runtests
from queue import PriorityQueue


def adj_list(edges, n):
    graph = [[] for _ in range(n + 1)]
    for u, v, dist in edges:
        graph[u].append((dist, v))
        graph[v].append((dist, u))
    return graph


def djikstra(graph, anomaly, start, end):
    n = len(graph)
    distance = [float("inf") for _ in range(n)]
    Q = PriorityQueue()
    distance[start] = 0
    Q.put((0, start))
    while not Q.empty():
        curr_ver = Q.get()[1]
        if curr_ver in anomaly:
            for tp in anomaly:
                if distance[tp] > distance[curr_ver]:
                    distance[tp] = distance[curr_ver]
                    Q.put((distance[tp], tp))
                    if tp == end:
                        return distance[curr_ver]
        for time, neighbour in graph[curr_ver]:
            if distance[neighbour] > distance[curr_ver] + time:
                distance[neighbour] = distance[curr_ver] + time
                Q.put((distance[neighbour], neighbour))

    if distance[end] == float("inf"):
        return None
    return distance[end]


def spacetravel(n, E, S, a, b):
    graph = adj_list(E, n)
    time = djikstra(graph, S, a, b)
    return time


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
