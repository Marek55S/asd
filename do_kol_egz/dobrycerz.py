# zadanie z egzaminu 3 22/23
# Dobrycerz (czyli rycerz, który zawsze uprzejmie mówi “dzień dobry”) chce się przedostać z zamku s
# do zamku t. Mapa zamków dana jest w postaci grafu nieskierowanego G, gdzie każda krawędź ma wa-
# gę oznaczającą ile godzin potrzeba, żeby ją przebyć. Wagi to liczby naturalne ze zbioru {1, 2, . . . , 8}.
# Po najdalej 16 godzinach podróży Dobrycerz musi nocować w zamku. Warunki uprzejmości wy-
# magają, żeby spędził w takim zamku 8 godzin (przejazd przez zamki, w których nie nocuje nie
# kosztuje dodatkowego czasu; szybko mówi “dzień dobry” strażnikom i jedzie dalej). Mapa z której
# korzysta Dobrycerz ma to do siebie, że liczba dróg jest proporcjonalna do liczby zamków. Czyli jeśli
# zamków jest n, to wiadomo, że dróg jest O(n).
# Zadanie polega na implementacji funkcji:
# goodknight( G, s, t )
# która na wejściu otrzymuje graf opisujący mapę zamków, reprezentowany w postaci macierzy są-
# siedztwa (czyli G[i][j] to liczba godzin, konieczna do przejechania bezpośrednio z zamku i do
# zamku j; w przypadku braku drogi G[i][j] = −1), zamek startowy s oraz zamek docelowy t, i
# zwraca minimalny czas (wyrażony w godzinach) potrzebny na przejazd z s do t (Dobrycerz nigdy
# nie musi nocować ani w zamku s ani w zamku t). Można założyć, że zawsze istnieje trasa z zamku
# s do t.
from queue import PriorityQueue


G = [
    [-1, 3, 8, -1, -1, -1],  # 0
    [3, -1, 3, 6, -1, -1],  # 1
    [8, 3, -1, -1, 5, -1],  # 2
    [-1, 6, -1, -1, 7, 8],  # 3
    [-1, -1, 5, 7, -1, 8],  # 4
    [-1, -1, -1, 8, 8, -1],  # 5
]


# dziala
# praktycznie takie samo zadanie tyle, ze z kolokwium 2 23/24
def dijkstra(G, s, t):
    q = PriorityQueue()
    dist = [[float("inf") for _ in range(17)] for __ in range(len(G))]
    for i in range(17):  # inicjalizacja dystansu w wierzchołku startowym
        dist[s][i] = 0

    def relax(u, v, weight, energy):
        if weight > energy:  # gdy brakuje nam energii zeby przejść do v
            if dist[u][energy] + weight + 8 < dist[v][16 - weight]:
                dist[v][16 - weight] = dist[u][energy] + weight + 8
                q.put((dist[v][16 - weight], v, 16 - weight))
        else:
            if dist[u][energy] + weight < dist[v][energy - weight]:
                dist[v][energy - weight] = dist[u][energy] + weight
                q.put((dist[v][energy - weight], v, energy - weight))

    q.put((0, s, 16))  # (distance,vertice,energy)
    visited = [[False for _ in range(17)] for __ in range(len(G))]
    while not q.empty():
        d, u, energy = q.get()
        if visited[u][energy]:
            continue
        visited[u][energy] = True
        for v, weight in G[u]:
            relax(u, v, weight, energy)
    return min(dist[t])


def edges_to_adjlist(E):  # zamiana na listę sąsiedztwa
    def find_max(E):
        maxi = -1
        for u, v, w in E:
            maxi = max(maxi, u, v)
        return maxi

    size = find_max(E) + 1
    G = [[] for _ in range(size)]

    for u, v, w in E:
        G[u].append((v, w))
        G[v].append((u, w))
    return G


def warrior(G, s, t):
    G = edges_to_adjlist(G)
    return dijkstra(G, s, t)


from collections import deque


def mapGraph(G):
    #
    n = len(G)
    D = [[] for _ in range(n)]

    for vertex in range(n):
        for neighbour in range(n):

            if G[vertex][neighbour] != -1:
                D[vertex].append((neighbour, G[vertex][neighbour]))

    # end 'for' loops

    return D


# end procedure 'mapGraph()'


def BFS(G, s, t):
    #
    n = len(G)

    distance = [[float("inf") for _ in range(17)] for _ in range(n)]
    distance[s][0] = 0

    queue = deque()
    queue.appendleft((s, 0, 0))

    while queue:
        vertex, value, time = queue.popleft()

        if value > 0:
            queue.append((vertex, value - 1, time))
        else:

            for neighbour, weight in G[vertex]:

                if distance[vertex][time] + weight + 8 < distance[neighbour][weight]:
                    distance[neighbour][weight] = distance[vertex][time] + weight + 8
                    queue.append((neighbour, weight, weight))

                if time + weight <= 16:
                    if (
                        distance[vertex][time] + weight
                        < distance[neighbour][time + weight]
                    ):
                        distance[neighbour][time + weight] = (
                            distance[vertex][time] + weight
                        )
                        queue.append((neighbour, weight, time + weight))

            # end 'for' clause
        # end 'if' clause
    # end 'while' loop

    return min(distance[t])


# end procedure 'BFS()'


def goodknight(G, s, t):
    #
    D = mapGraph(G)
    return BFS(D, s, t)
