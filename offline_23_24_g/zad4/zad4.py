# Marek Swakoń
# testy garkowe 10/10 w 0.03s, ale normalne testy 9/10 przekroczenie czasu
""" Moj algorytm zaczyna sio w funkcji Flight, ktora za pomoca funkcji build_adj buduje liste sasiedztwa. Potem uruchamia funkcje DFS na kazdej
krawedzi wychodzacej z podanego wierzcholka startowego wyszukujac krawedz miedzy zadanymi wierzcholkami funkcja fedge2. Dla niektorych 
przypadkow wywoluje rekurencyjna funkcje find_edge (ktora jest szybsza, ale dziala nie dla wszystkich przypadkow), jezeli funkjca wyrzuci
blad, to szukanie krawedzi odbywa sie na calej liscie krawedzi, jezeli funkcja zadziala, jest to znacznie usprawniane.
Funkcja DFS buduje graf w postaci listy sasiedztwa, deklaruje tablice visited, ktora bedzie przechowywac informacje o tym czy wierzcholek
zostal wczesniej odwiedzony oraz tworzy stos stack, ktory przechowuje informacje o odwiedzanych krawedziach oraz minimalna i maksymalna
dopuszczalna wysokosc w aktualnej scierzce krawedzi. Nastepnie wywolywana jest petla while dzialajaca dopuki stos nie jest pusty.
W petli pobierana jest ostatnia wartosc ze stosu, zapisywany jest stan odwiedzenia wierzcholkow oraz sprawdzany jest warunek konca.
Nastepnie wywolywana jest kolejna petla. Petla for sprawdza sasiadow wierzcholka, do ktorego prowadzi ostatnia przebyta krawedz, jesli 
jeszcze nie zostali odwiedzeni oraz mieszcza sie w aktualnym przedziale pulapu, to krawedz jest dodawana do stosu. Jezeli stos na koncu
petli pozostanie pusty, while skonczy sie wykonywac i zostanie zwrocone False
Zlozonosc czasowa algorytmu to  O(E^2+V*E), a pamieciowa O(V)"""
from zad4testy import runtests


def build_adj(edges):
    max_ver = 0
    for i in edges:
        se, en, val = i
        max_ver = max(max_ver, en)
    graph = [[] for _ in range(max_ver + 1)]
    for i in edges:
        (u, v, trash) = i
        if u not in graph[v]:
            graph[v].append(u)
        if v not in graph[u]:
            graph[u].append(v)
    return graph


def find_edge(edges, vstart, left, right):
    if left <= right:
        mid = (left + right) // 2
        first, sec, trash = edges[mid]
        first = min(first, sec)
        if first == vstart - 1:
            return mid
        elif first > vstart - 1:
            return find_edge(edges, vstart, left, mid - 1)
        else:
            return find_edge(edges, vstart, mid + 1, right)
    else:
        mid = (0 + len(edges)) // 2
        first, sec, trash = edges[mid]
        if first > vstart - 1:
            return 0
        else:
            return mid + 1


def fedge2(edges, vstart, vend):
    if vstart <= 1:
        prev = 0
    else:
        prev = find_edge(edges, vstart, 0, len(edges))
        if prev == -1:
            prev = 0
    for i in range(prev, len(edges)):
        edg = edges[i]
        v, u, trash = edg
        if max(u, v) == vend and min(u, v) == vstart:
            return i


def DFS(ledg, start_edge, end_ver, diff):
    graph = build_adj(ledg)
    maxver = len(graph)
    visited = [False for _ in range(maxver)]
    # parent = [None for _ in range(maxver)]
    # wierzcholek startoowy krawedzi, wierzcholek docelowy krawedzi, dolna granica pulapu, gorna granica pulapu
    stack = [
        (
            start_edge[0],
            start_edge[1],
            start_edge[2] - 2 * diff,
            start_edge[2] + 2 * diff,
        )
    ]
    while stack:
        (st_ver, e_ver, flr, ceil) = stack.pop()
        # print(st_ver, e_ver, flr, ceil)
        visited[st_ver] = True
        # sprawdzenie czy wierzcholek do ktorego prowadzi krawedz zostala juz odwiedzona
        if visited[e_ver] is not True:
            visited[e_ver] = True
            # warunek koncowy znalezienia odpowiedniej drogi
            if e_ver == end_ver:
                return True
            for i in range(len(graph[e_ver])):
                neighbour = graph[e_ver][i]
                ngb_edge = ledg[
                    fedge2(ledg, min(e_ver, neighbour), max(neighbour, e_ver))
                ]
                if (
                    visited[neighbour] == False
                    and ngb_edge[2] >= flr
                    and ngb_edge[2] <= ceil
                ):
                    stack.append(
                        (
                            e_ver,
                            neighbour,
                            max(flr, ngb_edge[2] - 2 * diff),
                            min(ceil, ngb_edge[2] + 2 * diff),
                        )
                    )
    return False


def Flight(L, x, y, t):
    G = build_adj(L)
    for i in G[x]:
        v = L[fedge2(L, min(x, i), max(x, i))]
        if DFS(L, v, y, t):
            return True
    return False


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(Flight, all_tests=True)
