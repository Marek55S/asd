# Marek Swakoń
# testy 10/10 czas 0.26
# W moim algorytmie korzystam z sortowania przez wstawianie(instertion sort). Najpierw sprawdzam, czy lista ma
# więcej niż 1 element. Następnie tworzę początek nowej listy, która będzie listą wynikową.
# Potem, implementuję pentlę, wpisuje sortuje i wpisuje do listy wynikowej pierwsze k elementow, abbym mógł w kolejnej
# pętli, w sortowaniu, mógł sprawdzać tylko ostatnie k elementów. Kolejna pętla sortuje resztę elementów mechanizmem
# insertion sort, ale sprawdzając jedynie ostatnie k elementów posortowanej listy.
# Funkcja zwraca początek posortowanej listy wynikowej
# Algorytm ten powinien mieć złożoność O(nk)


from zad1testy import Node, runtests


def SortH(p, k):
    # sprawdzenie przypadku brzegowego listy pustej lub 1 elementowej
    if p is None or p.next is None:
        return p
    # stworzenie początku listy wynikowej oraz wpisanie do niej pierwszego elementu
    newlist = Node()
    newlist.next = p
    cur = p.next
    p.next = None
    # petla sortujaca pierwsze k elementow
    cnt = 1
    while cnt < k and cur is not None:
        elem = newlist
        nxt = cur.next
        while elem.next is not None and elem.next.val < cur.val:
            elem = elem.next
        temp = elem.next
        elem.next = cur
        cur.next = temp
        cur = nxt
        cnt += 1

    # pętla sortująca resztę listy, sprawdzjąc ostatnie k elementów listy wynikowej
    kelem = newlist
    while cur is not None:
        elem = kelem
        nxt = cur.next
        while elem.next is not None and elem.next.val < cur.val:
            elem = elem.next
        temp = elem.next
        elem.next = cur
        cur.next = temp
        cur = nxt
        kelem = kelem.next
    return newlist.next


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(SortH, all_tests=True)
