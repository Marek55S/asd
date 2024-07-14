def partition(array, left, right):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[right], array[i + 1] = array[i + 1], array[right]
    return i + 1


def quicksort(array, left, right):
    if left < right:
        piv_idx = partition(array, left, right)
        quicksort(array, left, piv_idx - 1)
        quicksort(array, piv_idx + 1, right)


tab = [2, 1, 1, 5, 9, 4, 10, 2, 0, 83]
quicksort(tab, 0, 9)
print(tab)
