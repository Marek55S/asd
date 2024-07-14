def selectsort(array):
    n = len(array)
    for i in range(n):
        for j in range(i, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


tab = [8, 7, 3, 4, 1, 6, 5, 0]
selectsort(tab)
print(tab)
