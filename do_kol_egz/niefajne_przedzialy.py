# termin 3 22/23
# Dany jest zbiór P = {[a0, b0], . . . , [an−1, bn−1]} zawierający n parami różnych przedziałów domknię-
# tych. Mówimy, że para przedziałów jest fajna jeśli albo jeden z nich zawiera się w drugim, albo są
# rozłączne. Jeśli para przedziałów nie jest fajna, to mówimy na nią niefajna.
# Zadanie polega na implementacji funkcji: uncool( P )
# która na wejściu otrzymuje zbiór przedziałów P (w postaci listy, gdzie każdy element jest postaci
# [ai, bi] i opisuje przedział domknięty) i zwraca parę indeksów (i, j) takich, że para przedziałów
# P [i], P [j] jest niefajna (można założyć, że taka para przedziałów zawsze istnieje).

# poprawne ale wolne
import copy


"""def partition(array, l, r, idx):
    pivot = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j][0] < pivot[0]:
            i += 1
            array[j], array[i] = array[i], array[j]
            idx[j], idx[i] = idx[i], idx[j]
        elif array[j][0] == pivot[0] and array[j][1] < pivot[1]:
            array[j], array[i] = array[i], array[j]
            idx[j], idx[i] = idx[i], idx[j]
    array[r], array[i + 1] = array[i + 1], array[r]
    idx[r], idx[i + 1] = idx[i + 1], idx[r]
    return i + 1


def quicksort(array, left, right, idx):
    if left < right:
        pivot_idx = partition(array, left, right, idx)
        quicksort(array, left, pivot_idx - 1, idx)
        quicksort(array, pivot_idx + 1, right, idx)"""


def uncool(P):
    n = len(P)
    fpos = copy.deepcopy(P)
    # spos = copy.deepcopy(P)
    # fidx = [i for i in range(n)]
    # sidx = [i for i in range(n)]
    # quicksort(fpos, 0, n - 1, fidx)
    # quicksort(spos, 0, n - 1, 1, sidx)
    for i in range(n):
        for j in range(i, n):
            if P[i][0] < P[j][0] and P[j][0] <= P[i][1] and P[i][1] < P[j][1]:
                return (i, j)


P = [[1, 3], [6, 7], [2, 6], [4, 6], [1, 8], [5, 10]]
P2 = [
    [406, 678],
    [682, 764],
    [1, 400],
    [397, 400],
    [560, 2033],
    [260, 347],
    [1498, 2977],
    [350, 394],
    [1, 254],
    [1, 858],
]
print(uncool(P2))


def findBinFirst(tab, el, indeks):
    p = 0
    k = len(tab) - 1
    while p <= k:
        s = (p + k) // 2
        if tab[s][indeks] < el:
            p = s + 1
        else:
            k = s - 1
    if p < len(tab) and el == tab[p][indeks]:
        return p
    return -1


def find(T, x):
    n = len(T)
    i = -1
    k = -1
    for j in range(n):
        if T[j] == x:
            i = j
        elif (T[j][0] < x[0] and x[0] < T[j][1] < x[1]) or (
            x[1] > T[j][0] > x[0] and T[j][1] > x[1]
        ):
            k = j
        if i > -1 and k > -1:
            return i, k
    return -1, -1


def uncool2(P):
    n = len(P)
    pa = sorted(P, key=lambda x: x[0])
    pb = sorted(P, key=lambda x: x[1])
    for i in range(n):
        start = findBinFirst(pa, pa[i][0] + 1, 0)
        end = findBinFirst(pa, pa[i][1], 0)
        sa = end - start
        finA = findBinFirst(pb, pa[i][1] + 1, 1)
        startB = findBinFirst(pa, pa[i][0] + 1, 0)
        dom = finA - startB
        dom = dom if dom >= 0 else 0
        if sa > dom:
            # print(pa[i],'p')
            a, b = find(P, pa[i])
            if a > -1 and b > -1:
                return a, b

        start = findBinFirst(pa, pa[i][0] + 1, 1)
        end = findBinFirst(pa, pa[i][1], 1)
        sa = end - start
        if sa > dom:
            # print(pa[i],'k')
            a, b = find(P, pa[i])
            if a > -1 and b > -1:

                return a, b

    return -1, -1
