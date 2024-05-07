def skladowe(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    stack = []

    # dfs dopisujacy do stacka wierzcholek po przetworzeniu
    def dfs(curr):
        nonlocal graph, stack
        visited[curr] = True
        for neighbour in graph[curr]:
            if not visited[neighbour]:
                dfs(neighbour)
        stack.append(curr)

    # wywoluje dfs, aby wszystkie wierzcholki zostaly odwiedzone
    for v in range(n):
        if not visited[v]:
            dfs(v)
    # tworzy graf z odwroconymi krawedziami
    transposed = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            transposed[v].append(u)

    # resetuje tablice visited
    visited = [False for _ in range(n)]
    all_comp = []
    # petla wykonujaca sie dopuki stack nie jest pusty
    while stack:
        # pobiera i usuwa wierzcholek od najpozniej przetworzonego
        v = stack.pop()
        # tworzy tablice dla nowej spojnej skladowej i przechodzi po spojnej skladowej do ktorej nalezy v
        # i dodaje wierzcholki po ktorych przechodzi do utworzonej tablicy
        if not visited[v]:
            comp = []
            stack2 = [v]
            # przechodzi po spojnej skladowej
            while stack2:
                v = stack2.pop()
                # ten if chyba nie potrzebny
                # if visited[v]:
                #    continue
                visited[v] = True
                comp.append(v)
                # dodaje sasiadow v do stack2 ktory porusza sie po aktualnie przegladanej spojnej skladowej
                for u in transposed[v]:
                    if not visited[u]:
                        stack2.append(u)
            # dodaje utworzona spojna skladowa do listy wszystkich spojnych skladowych
            all_comp.append(comp)

    return all_comp


G = [[1, 7], [2], [0, 3], [6], [3, 9], [4, 8], [5], [8], [9], [7, 10], [8]]
print(skladowe(G))
