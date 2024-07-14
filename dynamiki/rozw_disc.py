# dziala ale nie wysylaj


def maze(L):
    n = len(L)
    dmat = [[None for _ in range(n)] for _ in range(n)]
    gmat = [[None for _ in range(n)] for _ in range(n)]

    def spacecheck(row, col):
        nonlocal n, L
        if row < 0 or row >= n:
            return False
        if col < 0 or col >= n:
            return False
        elif L[row][col] == "#":
            return False
        return True

    def ffun(row, col):
        nonlocal L
        if row == 0 and col == 0:
            return 0
        elif not spacecheck(row, col):
            return float("-inf")
        return max(dfun(row, col), gfun(row, col))

    def gfun(row, col):
        nonlocal L
        if row == 0 and col == 0:
            return 0
        elif not spacecheck(row, col):
            return float("-inf")
        elif gmat[row][col] is not None:
            return gmat[row][col]
        else:
            gmat[row][col] = max(ffun(row, col - 1), gfun(row - 1, col)) + 1
            return gmat[row][col]

    def dfun(row, col):
        nonlocal L
        if row == 0 and col == 0:
            return 0
        elif not spacecheck(row, col):
            return float("-inf")
        if dmat[row][col] is not None:
            return dmat[row][col]
        else:
            dmat[row][col] = max(ffun(row, col - 1), dfun(row + 1, col)) + 1
            return dmat[row][col]

    result = ffun(n - 1, n - 1)
    return result if result != float("-inf") else -1


L = ["....", "..#.", "..#.", "...."]
print(maze(L))
