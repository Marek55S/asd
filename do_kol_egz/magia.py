# 21/22 term 2
"""Magiczny Wojownik obudził się w komnacie 0 pewnej tajemniczej jaskini, mając w głowie jedynie
instrukcje, jakie otrzymał od Złego Maga. Wie, że komnaty są ponumerowane od 0 do n − 1 i w
każdej komnacie znajduje się troje drzwi, z których każde pozwala przejść do komnaty o wyższym
numerze (cofnięcie się do komnaty o niższym numerze grozi śmiercią Wojownika; co więcej, niektóre
drzwi są zablokowane) oraz skrzynia z pewną liczbą sztabek złota. Wstępnie wszystkie drzwi są
zamknięte, ale jeśli w skrzyni zostanie umieszczona odpowiednia liczba sztabek złota, to drzwi się
otwierają i można nimi przejść. Z każdej skrzyni można zabrać najwyżej 10 sztabek złota, ale można
też w niej zostawić dowolnie wiele sztabek. Na początku Wojownik nie ma ani jednej sztabki a jego
celem (na zlecenie Złego Maga) jest dojść do komnaty n − 1 mając jak najwięcej sztabek.
Zadanie polega na zaimplementowaniu funkcji:
def magic( C )
która otrzymuje na wejściu tablicę C opisującą jaskinię (n = ∣C∣) i zwraca największą liczbę sztabek
złota, z którymi Wojownik może dojść do komnaty n − 1, lub −1 jeśli dotarcie do tej komnaty jest
niemożliwe. Opis jaskini jest postaci C = [R0, . . . , Rn−1], gdzie każde Ri to opis komnaty postaci:
[G, [K0, W0], [K1, W1], [K2, W2]]
gdzie G to liczba sztabek złota w skrzyni a każda para [Ki, Wi] składa się z liczby Ki sztabek słota
potrzebnych do otwarcia drzwi numer i prowadzących do komnaty Wi (gdzie Wi > i lub Wi = −1
jeśli za tymi drzwiami jest lita skała i nie da się nimi przejść nawet jeśli się je otworzy). Funkcja
powinna być możliwie jak najszybsza."""


def magic(C):
    n = len(C)
    dp = [-1 for _ in range(n)]
    dp[0] = 0

    for i in range(n):
        for j in range(1, 4):
            obecna_komnata = i
            ile_w_skrzyni = C[i][0]
            nowa_komnata = C[i][j][1]
            ile_ma_byc_w_skrzyni = C[i][j][0]

            if (
                nowa_komnata > obecna_komnata
                and dp[obecna_komnata] != -1
                and ile_w_skrzyni - ile_ma_byc_w_skrzyni <= 10
            ):
                dp[nowa_komnata] = max(
                    dp[nowa_komnata],
                    dp[obecna_komnata] + ile_w_skrzyni - ile_ma_byc_w_skrzyni,
                )

    return dp[-1]


C = [
    [8, [6, 3], [4, 2], [7, 1]],  # 0
    [22, [12, 2], [21, 3], [0, -1]],  # 1
    [9, [11, 3], [0, -1], [7, -1]],  # 2
    [15, [0, -1], [1, -1], [0, -1]],
]  # 3
print(magic(C))
