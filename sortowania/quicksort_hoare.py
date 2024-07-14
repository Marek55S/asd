def partition(array, left, right):
    pivot = array[(left + right) // 2]
    # print(pivot, array[left : right + 1])
    i = left - 1
    j = right + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


def quicksort(array, left, right):
    if left < right:
        piv_idx = partition(array, left, right)
        quicksort(array, left, piv_idx)
        quicksort(array, piv_idx + 1, right)


tab = [2, 1, 1, 5, 9, 4, 10, 2, 0, 83]
quicksort(tab, 0, 9)
print(tab)
