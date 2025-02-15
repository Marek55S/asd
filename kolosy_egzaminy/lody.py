# zjesc jak najwiecej lodow przed roztopieniem, w czasie 1 zjedzonych lodow topi sie 1 jednostka
# obj we wszystkich innych


def Partition(T, left, right):
    #
    a = left - 1

    for b in range(left, right):
        if T[b] <= T[right]:
            a += 1
            T[b], T[a] = T[a], T[b]
    #

    a += 1
    T[a], T[right] = T[right], T[a]
    return a


# end procedure Partition()


def quickSort(T, left, right):
    #
    if left < right:
        pivot = Partition(T, left, right)
        quickSort(T, left, pivot - 1)
        quickSort(T, pivot + 1, right)
    #


# end procedure quickSort()


def ice_cream(T):
    #
    quickSort(T, 0, len(T) - 1)
    # T = MergeSort(T)
    a = len(T) - 1
    maxVolume = 0
    time = 0

    while a >= 0 and T[a] - time > 0:
        maxVolume += T[a] - time
        a -= 1
        time += 1
    #

    return maxVolume


arr = [6, 34, 5, 6, 2, 1, 4]
quickSort(arr, 0, 6)
print(arr)
