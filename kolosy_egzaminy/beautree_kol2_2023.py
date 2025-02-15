#   Dany jest ważony, nieskierowany graf G =(V, E), którego wagi krawędzi opisuje funkcja w E →N.
#    Wiadomo, że wagi krawędzi są parami różne. Niech T będzie pewnym drzewem rozpinającym G,
#    m będzie najmniejszą wagą krawędzi z T a M będzie największą wagą krawędzi z T. Mówimy, że
#    T jest piękne jeśli każda krawędź spoza T albo ma wagę mniejszą niż m albo większą niż M. Wagą
#    drzewa rozpinającego jest suma wag jego krawędzi. Zadanie polega na implementacji funkcji
#    beautree( G )
#    która na wejściu otrzymuje graf reprezentowany w postaci listowej i zwraca wagę najlżejszego pięk-
#    nego drzewa rozpinającego G lub None jeśli takie drzewo nie istnieje.


# duza zlozonosc, testy przechodzi ok 6,3s
# mozna by zoptymalizowac jakos
from collections import deque


def to_edg_list(graph):
    n = len(graph)
    edges = []
    for u in range(n):
        for v, w in graph[u]:
            if u < v:
                edges.append((u, v, w))
    return edges


def to_nlist(graph, n):
    nlist = [[] for _ in range(n)]
    for u, v, w in graph:
        nlist[v].append((u))
        nlist[u].append((v))
    return nlist


def cycle(edges, n):
    print(edges)
    vertices = set()
    for u, v, _ in edges:
        if u not in vertices:
            vertices.add(u)
        if v not in vertices:
            vertices.add(v)
    if len(vertices) != n:
        return False
    return True


def is_tree(edges, n):
    graph = to_nlist(edges, n)
    visited = [False for _ in range(n)]
    queue = deque()
    queue.append(0)
    visited[0] = True
    while queue:
        curr = queue.popleft()
        for nbr in graph[curr]:
            if not visited[nbr]:
                visited[nbr] = True
                queue.append(nbr)
    for i in range(n):
        if not visited[i]:
            return False
    return True


def beautree(G):
    graph = to_edg_list(G)
    nedg = len(graph)
    graph.sort(key=lambda x: x[2])
    minedg = len(G) - 1
    tree = deque()
    for i in range(0, minedg):
        tree.append(graph[i])
    for i in range(0, nedg - minedg):
        if is_tree(tree, minedg + 1):
            return sum(w for _, _, w in tree)
        tree.append(graph[minedg + i])
        tree.popleft()
    return None


G = [
    [(1, 2), (2, 3)],  # 0
    [(0, 2), (2, 1), (3, 5), (4, 6)],  # 1
    [(0, 3), (1, 1), (3, 9), (4, 4)],  # 2
    [(1, 5), (2, 9), (4, 10), (5, 8)],  # 3
    [(2, 4), (1, 6), (3, 10), (5, 7)],  # 4
    [(3, 8), (4, 7)],
]  # 5
G2 = to_edg_list(G)
G3 = [
    (1, 2, 1),
    (0, 1, 2),
    (0, 2, 3),
    (2, 4, 4),
    (1, 3, 5),
    (1, 4, 6),
    (4, 5, 7),
    (3, 5, 8),
    (2, 3, 9),
    (3, 4, 10),
]
print(beautree(G))


class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0

    #


# end Class


def Find(x):
    #
    if x.parent != x:
        x.parent = Find(x.parent)
    #
    return x.parent


# end procedure Find()


def Union(X, Y):  # X - root, Y - root
    #
    if X.rank > Y.rank:
        Y.parent = X

    elif X.rank < Y.rank:
        X.parent = Y

    else:
        X.parent = Y
        Y.rank += 1


# end procedure Union()


def Kruskal(G, Edges, i):
    #
    n = len(G)
    minSpanningTree = []
    Vertices = [Node(v) for v in range(n)]

    sumMST = 0

    for edge in Edges[i : len(Edges)]:
        #
        a, b, weight = edge
        rootA, rootB = Find(Vertices[a]), Find(Vertices[b])

        if rootA != rootB:
            Union(rootA, rootB)
            minSpanningTree.append(edge)
            sumMST += weight
        # end if

        if len(minSpanningTree) == n - 1:
            return minSpanningTree, sumMST

    # end for

    return None, None


# end procedure Kruskal()


def getEdgesList(G):
    #
    edges = []

    for vertex in range(len(G)):
        for neighbour, weight in G[vertex]:
            if vertex < neighbour:
                edges.append((vertex, neighbour, weight))
    # end 'for' loops

    return edges


# end procedure getEdgesList()


def checkEdgesCondition(Edges, minSpanningTree, minEdgeValue, maxEdgeValue, i):
    #
    for edge in Edges[i : i + len(minSpanningTree)]:
        if edge not in minSpanningTree:
            a, b, weight = edge
            if minEdgeValue <= weight <= maxEdgeValue:
                return False
    #
    return True


# end procedure checkEdges()


def beautree2(G):
    #
    n = len(G)

    Edges = getEdgesList(G)
    Edges.sort(key=lambda x: x[2])

    minSumMST = float("inf")  # suma wag krawedzi najmniejszego MST

    for i in range(len(Edges)):
        #
        minSpanningTree, sumMST = Kruskal(G, Edges, i)

        if minSpanningTree != None:
            #
            minEdgeValue = minSpanningTree[0][2]
            maxEdgeValue = minSpanningTree[n - 2][2]

            if checkEdgesCondition(
                Edges, minSpanningTree, minEdgeValue, maxEdgeValue, i
            ):
                minSumMST = min(minSumMST, sumMST)

        # end 'if' clauses
    # end 'for' loop

    if minSumMST != float("inf"):
        return minSumMST
    return None
