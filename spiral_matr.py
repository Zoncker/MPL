def spiral_matr(n, m):
    count = 0
    res = [[0 for i in range(m)] for j in range(n)]
    k = 1
    for i in range(n * m):

        for j in range(k - 1, m - k + 1):
            count += 1
            res[k - 1][j] = count
            i += 1

        for j in range(k, n - k + 1):
            count += 1
            res[j][m - k] = count
            i += 1

        for j in reversed(range(k - 1, m - k)):
            count += 1
            res[n - k][j] = count
            i += 1

        for j in reversed(range(k, n - k)):
            count += 1
            res[j][k - 1] = count
            i += 1

        k += 1

    return res


def main():
    n, m = map(int, input("enter the dimensions of the matrix:").split())
    res = spiral_matr(n, m)
    for s in res:
        print(*s)


if __name__ == '__main__':
    main()
