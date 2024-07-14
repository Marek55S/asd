# Do elektrowni ma przyjechać seria długo oczekiwanych tranportów węgla. Każdy transport zawiera
# pewną liczbę ton węgla, które muszą być składowane w jednym z magazynów o numerach 0, 1,
# 2, . . . (magazynów jest bardzo dużo i na pewno wystarczą na cały węgiel). Każdy magazyn ma
# pojemność T ton i węgiel z każdego transportu musi być przechowywany razem, w jednym maga-
# zynie (ale w danym magazynie może być węgiel z kilku różnych transportów). Dyrekcja elektrowni
# przyjęła zasadę, że gdy przyjeżdża kolejny transport, to węgiel umieszczany jest w magazynie o
# najniższym numerze, w którym się mieści (na szczęście żaden transport nie ma więcej niż T ton).
# Proszę napisać funkcję: def coal( A, T )
# która przyjmuje na wejściu tablicę A = [a0, . . . , an−1] zawierającą ilości węgla w kolejnych transpor-
# tach (wyrażoną w tonach, jako liczby naturalne) oraz liczbę naturalną T oznaczającą pojemność
# każdego z magazynów. Funkcja powinna zwrócić numer magazynu, w którym umieszczono ostatni transport.


# cos tu smierdzi, szczegolnie jesli chodzi o testy
def partition(array, l, r):
    pivot = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] > pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def quicksort(array, left, right):
    if left < right:
        pivot_idx = partition(array, left, right)
        quicksort(array, left, pivot_idx - 1)
        quicksort(array, pivot_idx + 1, right)


def coal(A, T):
    n = len(A)
    storage = [T for _ in range(n + 1)]
    quicksort(A, 0, n - 1)
    for i in range(n):
        j = 0
        while storage[j] - A[i] < 0:
            j += 1
        storage[j] -= A[i]
    mnr = 0
    while storage[mnr] < T:
        mnr += 1
    return mnr - 1


A = [1, 6, 2, 10, 8, 7, 1]
T = 10
print(coal(A, T))
