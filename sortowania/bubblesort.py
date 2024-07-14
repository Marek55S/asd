def bubblesort(array):
    n = len(array)
    swapped = False
    for i in range(0, n - 1):
        for j in range(i, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swapped = True
        if not swapped:
            return


tab = [8, 7, 6, 5, 4, 3, 2, 1]
bubblesort(tab)
print(tab)
