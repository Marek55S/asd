# Marek Swakoń
# Mój algorytm najpierw sortuje listy X oraz Y, aby upewnić się, że dalsza część algorytmu
# zadziała poprawnie. Następnie tworzy tablicę która będzie przechowywać wyniki liczonych
# podproblemów. Potem, iteruje przez stworzoną tablicę i wypełnia ją minimalną sumą odległości
# parkingów od wieżowców dla miejsca w tablicy określonego współrzędnymi i,j rozważając
# pierwsze i wierzowców oraz j parkingów w posortowanych rosnąco tablicach.
# na końcu funkcja zwraca wartość tablicy wynikowej dla współrzędnych n-1,m-1, czyli
# wynik całego problemu, uwzględniającego całe tablice X oraz Y.
# Złożoność czasowa problemu to O(m*n), złożoność pamięciowa to (m*n)

from zad8testy import runtests


def parking(X, Y):
    X.sort()
    Y.sort()
    n = len(X)
    m = len(Y)
    ftab = [[float("inf") for _ in range(m)] for _ in range(n)]
    ftab[0][0] = abs(X[0] - Y[0])
    for i in range(1, m):
        ftab[0][i] = min(ftab[0][i - 1], abs(X[0] - Y[i]))
        if ftab[0][i] == ftab[0][i - 1]:
            ftab[0][i + 1 : m + 1] = [ftab[0][i]] * (m - i)
            break
    for i in range(1, n):
        for j in range(i, m):
            ftab[i][j] = min(ftab[i - 1][j - 1] + abs(X[i] - Y[j]), ftab[i][j - 1])
            if ftab[i][j] == ftab[i][j - 1]:
                ftab[i][j + 1 : m + 1] = [ftab[i][j]] * (m - i)
                break
    return ftab[n - 1][m - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)
