def insertionsort(array):
    n = len(array)
    for i in range(1, n):
        pos = i
        val = array[i]
        while pos > 0 and val < array[pos - 1]:
            array[pos] = array[pos - 1]
            pos -= 1
        array[pos] = val


tab = [8, 7, 3, 4, 1, 6, 5, 0]
insertionsort(tab)
print(tab)
