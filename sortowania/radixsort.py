def countingsort(array, dig):
    n = len(array)
    result = [None] * n
    cntarr = [0] * 10
    for i in array:
        cntarr[(i // dig) % 10] += 1
    for j in range(1, 10):
        cntarr[j] += cntarr[j - 1]
    i = n - 1
    while i >= 0:
        idx = array[i] // dig
        result[cntarr[idx % 10] - 1] = array[i]
        cntarr[idx % 10] -= 1
        i -= 1
    for i in range(n):
        array[i] = result[i]


def radixsort(array):
    dig = 1
    melem = max(array)
    while melem // dig > 0:
        countingsort(array, dig)
        dig *= 10


tab = [100, 123, 6543, 2, 43, 115, 486, 23456, 2345, 951, 564]
radixsort(tab)
print(tab)
