# algorytm rozwiązujący problem krapsack, mamy ograniczoną łączną masę przedmiotów
# i musimy upakować w niej przedmioty o największej łącznej wartości


# W - tablica wagi przedmiotów, P - tablica wartości przedmiotów, B - maksymalna waga plecaka
def krapsack(W, P, B):
    n = len(W)
    F = [[0 for _ in range(B + 1)] for _ in range(n)]
    for b in range(W[0], B + 1):
        F[0][b] = P[0]

    for b in range(B + 1):
        for i in range(1, n):
            F[i][b] = F[i - 1][b]
            if b - W[i] >= 0:
                F[i][b] = max(F[i][b], F[i - 1][b - W[i]] + P[i])
    return F[n - 1][B]


w = [2, 3, 4, 5]
p = [3, 4, 5, 6]
print(krapsack(w, p, 5))
