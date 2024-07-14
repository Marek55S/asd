# problem komiwojazera (TSP), wersja bitoniczna rzucona na plaszczyzne kartezjanska
# wziete z comrena podobno 1 do 1 wiec tam bedzie lepiej wytlumaczone

n = 10
D = [()]
F = [[float("inf")] * n for _ in range(n)]


def tspf(i, j, F, D):
    if F[i][j] != float("inf"):
        return F[i][j]
    if i == j - 1:
        best = float("inf")
        for k in range(j - 1):
            best = min(best, tspf(k, j - 1, F, D) + D[k][j])
        F[j - 1][j] = best
    else:
        F[i][j] = tspf(i, j - 1, F, D) + D[j - 1][j]
    return F[i][j]
