def mergesort(array, left, right):
    if left < right:
        mid = (left + right) // 2
        mergesort(array, left, mid)
        mergesort(array, mid + 1, right)
        merge(array, left, mid, right)


def merge(array, left, mid, right):
    leftlen = mid - left + 1
    rightlen = right - mid
    L = array[left : left + leftlen]
    R = array[mid + 1 : mid + 1 + rightlen]
    i = 0
    j = 0
    k = left
    while i < leftlen and j < rightlen:
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i < leftlen:
        array[k] = L[i]
        i += 1
        k += 1
    while j < rightlen:
        array[k] = R[j]
        j += 1
        k += 1


tab = [8, 7, 3, 4, 1, 6, 5, 0]
mergesort(tab, 0, 7)
print(tab)
