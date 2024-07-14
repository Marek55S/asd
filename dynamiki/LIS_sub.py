# najdluzszy rosnacy podciag


def lis(A):
    n = len(A)
    F = [1] * n
    P = [-1] * n
    maxf = 0
    for k in range(1, n):
        for t in range(k):
            if A[t] < A[k] and F[k] < F[t] + 1:
                F[k] = F[t] + 1
                P[k] = t
                maxf = k

    def print_sub(k):
        nonlocal P, F
        if P[k] != -1:
            print_sub(P[k])
        print(A[k])

    print_sub(maxf)
    print(" ")
    return F[maxf]


array = [2, 1, 4, 3, 4, 8, 5, 7]
print(lis(array))
