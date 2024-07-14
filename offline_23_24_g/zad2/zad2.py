# Marek Swakoń
# testy 5/10 za dlugi czas
# Mój algorytm opiera się na standardowym algorytmie select sort, w ktorej sprawdzam czy pivot zwrocony przez
# funkcje partition jest na j-tym miejsu w tablicy, jezeli tak nie jest, to funkcja wywoluje sie rekurencyjnie
# w odpowiedniej czesci tablicy. Funkcja ksum przechodzi iteracyjnie po zadanym zakresie tablicy T, przekazuje
# slice z tablicy T do funkcji kLargest i dodaje do sumy otrzymany wynik.
# pesymistyczna złożoność czasowa O((n-p+1)n)
from zad2testy import runtests


def partition(array, left, right):
    if left == right:
        return left
    pivot_index = right
    i = left
    for j in range(left, right):
        if array[j] > array[pivot_index]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[pivot_index] = array[pivot_index], array[i]
    return i


def kLargest(array, k, left, right):
    pivot = partition(array, left, right)
    if pivot == k - 1:
        return array[pivot]
    elif pivot > k - 1:
        return kLargest(array, k, left, pivot - 1)
    else:
        return kLargest(array, k, pivot + 1, right)


def ksum(T, k, p):
    n = len(T)
    sum = 0
    for i in range(0, n - p + 1):
        A = T[i : i + p]
        sum += kLargest(A, k, 0, p - 1)
    return sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)
