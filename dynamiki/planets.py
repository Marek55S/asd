# zadanie z egzaminu 2023 termin 2


def planets(D, C, T, E):
    n = len(D)
    fuel = [[float("inf") for _ in range(E + 1)] for _ in range(n)]
    for i in range(E + 1):
        fuel[0][i] = C[0] * i
    tp_planet = T[0][0]
    tp_price = T[0][1]
    fuel[tp_planet][0] = fuel[0][0] + tp_price
    for i in range(1, n):
        for j in range(E + 1):
            dist = D[i] - D[i - 1]
            if j + dist < E:
                price = fuel[i - 1][dist + 1]
            else:
                price = fuel[i - 1][E] + C[i] * (j + dist - E)
            price2 = fuel[i][j - 1] + C[i]
            fuel[i][j] = min(fuel[i][j], price, price2)
        tp_planet = T[i][0]
        tp_price = T[i][1]
        fuel[tp_planet][0] = min(fuel[tp_planet][0], fuel[i][0] + tp_price)
    return min(fuel[n - 1])
