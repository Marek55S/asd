def bubblesort(array):
    n = len(array)
    flag = True
    i = 0
    while flag and i < n:
        flag = False
        for j in range(1, n - i):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
                flag = True
        i += 1


def selectionsort(array):
    n = len(array)
    for i in range(n):
        minidx = i
        for j in range(i, n):
            if array[minidx] > array[j]:
                minidx = j
        array[i], array[minidx] = array[minidx], array[i]


def insertionsort(array):
    n = len(array)
    for i in range(n):
        j = i - 1
        val = array[i]
        while j >= 0 and array[j] > val:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = val


def merge(array, left, mid, right):
    leftlen = mid - left + 1
    rightlen = right - mid
    ltab = array[left : left + leftlen]
    rtab = array[mid + 1 : mid + rightlen + 1]
    i = 0
    j = 0
    k = left
    while i < leftlen and j < rightlen:
        if ltab[i] < rtab[j]:
            array[k] = ltab[i]
            i += 1
        else:
            array[k] = rtab[j]
            j += 1
        k += 1
    while i < leftlen:
        array[k] = ltab[i]
        i += 1
        k += 1
    while j < rightlen:
        array[k] = rtab[j]
        j += 1
        k += 1


def mergesort(array, l, r):
    if l < r:
        mid = (l + r) // 2
        mergesort(array, l, mid)
        mergesort(array, mid + 1, r)
        merge(array, l, mid, r)


def lchild(i):
    return 2 * i + 1


def rchild(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapify(array, n, i):
    left = lchild(i)
    right = rchild(i)
    maxind = i
    if left < n and array[left] > array[maxind]:
        maxind = left
    if right < n and array[right] > array[maxind]:
        maxind = right
    if maxind != i:
        array[i], array[maxind] = array[maxind], array[i]
        heapify(array, n, maxind)


def buildheap(array):
    n = len(array)
    for i in range(parent(n - 1), -1, -1):
        heapify(array, n, i)


def heapsort(array):
    n = len(array)
    buildheap(array)
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)


def partition(array, l, r):
    pivot = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def quicksort(array, l, r):
    if l < r:
        pivot_idx = partition(array, l, r)
        quicksort(array, l, pivot_idx - 1)
        quicksort(array, pivot_idx + 1, r)


def quickselect(array, k, l, r):
    if l <= r:
        pivot_idx = partition(array, l, r)
        if pivot_idx == k - 1:
            return array[pivot_idx]
        elif pivot_idx < k - 1:
            return quickselect(array, k, pivot_idx + 1, r)
        else:
            return quickselect(array, k, l, pivot_idx - 1)


def countingsort(array):
    k = max(array) + 1
    n = len(array)
    result = [None] * n
    counter = [0] * k
    for val in array:
        counter[val] += 1
    for i in range(1, k):
        counter[i] += counter[i - 1]
    for i in range(n - 1, -1, -1):
        result[counter[array[i]] - 1] = array[i]
        counter[array[i]] -= 1
    for i in range(n):
        array[i] = result[i]


def radixcount(array, pos):
    n = len(array)
    result = [None] * n
    counter = [0] * 10
    for i in range(n):
        counter[(array[i] // pos) % 10] += 1
    for j in range(1, 10):
        counter[j] += counter[j - 1]
    for i in range(n - 1, -1, -1):
        idx = array[i] // pos
        result[counter[idx % 10] - 1] = array[i]
        counter[idx % 10] -= 1
    for j in range(n):
        array[j] = result[j]


def radixsort(array):
    dig = 1
    melem = max(array)
    while melem // dig > 0:
        radixcount(array, dig)
        dig *= 10


def bucketsort(array):
    n = len(array)
    maxval = max(array)
    minval = min(array)
    bucketrange = (minval + maxval + 1) / n
    buckets = [[] for _ in range(n)]
    for val in array:
        bucketidx = int((val - minval) / bucketrange)
        buckets[bucketidx].append(val)
    for j in range(n):
        selectionsort(buckets[j])

    idx = 0
    for bucket in buckets:
        for val in bucket:
            array[idx] = val
            idx += 1


tab = [1, 3, 52, 4, 6, 1, 5, 2, 9, 56, 8]
tab2 = [0, 2, 1, 0, 1, 3, 2]
tab3 = [0.3, 0.1, 2, 0.95, 0.73, 0.66, 0.47]
bucketsort(tab3)
print(tab3)
