# zadanie z egzaminu 1 22/23
# Złycerz (czyli zły rycerz) wędruje po średniowiecznym grafie G = (V, E), gdzie waga każdej
# krawędzi to liczba sztabek złota, którą trzeba zapłacić za przejazd nią (myta, jedzenie, itp.). W
# każdym wierzchołku znajduje się zamek, który zawiera w skarbcu pewną daną liczbę sztabek
# złota. Złycerz może napaść na jeden zamek i zabrać całe jego złoto, ale od tego momentu
# zaczyna być ścigany i każdy przejazd po krawędzi jest dwa razy droższy, oraz dodatkowo na
# każdej drodze musi zapłacić r sztabek złota jako łapówkę (zatem od tej pory koszt przejazdu
# danej krawędzi jest równy dwukrotności wagi tej krawędzi plus wartość r). Co więcej, Złycerz nie
# może napaść więcej niż jednego zamku, bo jest trochę leniwy (oprócz tego, że zły). Proszę wska-
# zać trasę Złycerza z zamku s do t o najmniejszym koszcie (lub największym zysku, jeśli to możliwe).
# Uwaga. Złycerz może przejechać po danej krawędzi więcej niż raz (np. raz jadąc do zamku, który
# chce napaść, a potem z niego wracając).
# Zadanie polega na implementacji funkcji:
# gold( G,V,s,t,r )
# która na wejściu otrzymuje: graf G reprezentowany w postaci listowej, tablicę V zawierającą liczby
# sztabek złota w kolejnych zamkach, zamek początkowy s, zamek końcowy t oraz wysokość łapówki r.
# Funkcja powinna zwrócić najmniejszy koszt drogi uwzględniający ewentualny napad. Jeżeli zysk
# z napadu jest większy, od kosztu drogi należy, powstały zysk należy zwrócić jako liczbę ujemną

# zrobione dobrze - złożoność chyba wzorcowa
from queue import PriorityQueue


def djikstra(graph, start):
    n = len(graph)
    distance = [float("inf") for _ in range(n)]
    # parent = [None for _ in range(n)]

    queue = PriorityQueue()
    queue.put((0, start))
    distance[start] = 0
    while not queue.empty():
        _, curr = queue.get()
        for v, w in graph[curr]:
            if distance[v] > distance[curr] + w:
                distance[v] = distance[curr] + w
                # parent[v] = curr
                queue.put((distance[v], v))
    return distance


def penalty(graph, r):
    n = len(graph)
    aftergraph = [[] for _ in range(n)]
    for u in range(n):
        for v, w in graph[u]:
            aftergraph[u].append((v, 2 * w + r))
    return aftergraph


def gold(G, V, s, t, r):
    sdist = djikstra(G, s)
    robbed = penalty(G, r)
    tdist = djikstra(robbed, t)
    print(sdist, tdist)
    results = [0 for _ in range(len(G))]
    for i in range(len(G)):
        results[i] = V[i] - sdist[i] - tdist[i]
    return -max(results)


G = [
    [(1, 9), (2, 2)],  # 0
    [(0, 9), (3, 2), (4, 6)],  # 1
    [(0, 2), (3, 7), (5, 1)],  # 2
    [(1, 2), (2, 7), (4, 2), (5, 3)],  # 3
    [(1, 6), (3, 2), (6, 1)],  # 4
    [(2, 1), (3, 3), (6, 8)],  # 5
    [(4, 1), (5, 8)],
]  # 6

V = [25, 30, 20, 15, 5, 10, 0]
print(gold(G, V, 0, 6, 7))
