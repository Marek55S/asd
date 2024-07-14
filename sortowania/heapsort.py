def left(n):
    return 2 * n + 1


def right(n):
    return 2 * n + 2


def parent(n):
    return (n - 1) // 2


def heapify(array, n, i):
    lchild = left(i)
    rchild = right(i)
    max_ind = i
    if lchild < n and array[lchild] > array[max_ind]:
        max_ind = lchild
    if rchild < n and array[rchild] > array[max_ind]:
        max_ind = rchild
    if max_ind != i:
        array[i], array[max_ind] = array[max_ind], array[i]
        heapify(array, n, max_ind)


def buildheap(array):
    n = len(array)
    for i in range(parent(n - 1), -1, -1):
        heapify(array, n, i)


def heapsort(array):
    n = len(array)
    buildheap(array)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


tab = [2, 1, 1, 5, 9, 4, 10, 2, 0, 83]
heapsort(tab)
print(tab)
