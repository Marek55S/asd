# liczby fibonacciego dynamikiem


def fib_dyn(n):
    F = [0] * (n + 1)
    F[0] = 1
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]


def fib_rek(n):
    if n == 1 or n == 0:
        return 1
    return fib_rek(n - 1) + fib_rek(n - 2)


num = 14
print(fib_rek(num), fib_dyn(num))
