def countingsort(array):
    k = max(array)
    n = len(array)
    result = [None] * n
    cntarr = [0] * (k + 1)
    for i in array:
        cntarr[i] += 1
    for j in range(1, k + 1):
        cntarr[j] += cntarr[j - 1]
    for i in range(n - 1, -1, -1):
        result[cntarr[array[i]] - 1] = array[i]
        cntarr[array[i]] -= 1
    for i in range(n):
        array[i] = result[i]


tab = [1, 2, 0, 2, 3, 0, 4, 0]
countingsort(tab)
print(tab)
