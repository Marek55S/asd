# Marek Swakoń
# testy 10/10 czas 2.10
# Mój algorytm korzysta z zasady dzialania counting sorta. Funkcja counts tworzy tablice, ktora zlicza liczbe
# elementow mniejszych niz aktualny indeks tablicy, tak jak w counting sort.
# Funkcja domiance na poczatku tworzy 2 tablice, pierwsza zawiera wspolrzedne x, a druga wspolrzedne y,
# a pozniej przekazuje je do funkcji counts. Nastepnie wyszukuje w tablicy P maksymalna sume elementow
# mniejszych od x i y poprzez zsumowanie wartosci o indeksach o 1 mniejszych z tablic xarr i yarr.
# Gdy juz znajdziemy maksymalna sume, to wiemy ze element dla ktorego zostala ona policzona
# jest elementem, ktorego szukamy, wiec liczymy ile punktow dominuje i zwracamy otrzymany wynik.
# zlozonosc czasowa i pamieciowa algorytmu wynosi O(n)
from zad3testy import runtests


def counts(array):
    max_val = max(array)
    cnts = [0] * (max_val + 1)
    for num in array:
        cnts[num] += 1
    for i in range(1, len(cnts)):
        cnts[i] += cnts[i - 1]
    return cnts


def dominance(P):
    n = len(P)
    xarr = [i[0] for i in P]
    yarr = [i[1] for i in P]
    xarr = counts(xarr)
    yarr = counts(yarr)
    maxind = 0
    maxval = 0
    for i in range(n):
        sum = xarr[P[i][0] - 1] + yarr[P[i][1] - 1]
        if sum > maxval:
            maxval = sum
            maxind = i
    cnt = 0
    posx = P[maxind][0]
    posy = P[maxind][1]
    for j in range(0, n):
        curx, cury = P[j]
        if posx > curx and posy > cury:
            cnt += 1
    return cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(dominance, all_tests=True)
