if __name__ == '__main__':
    n, m, k = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a.append(list(map(int, input().split())))
        b.append([0 for j in range(m)])
    b[0][0] = a[0][0]
    for i in range(1, n):
        b[i][0] = b[i - 1][0] + a[i][0]
    for j in range(1, m):
        b[0][j] = b[0][j - 1] + a[0][j]
    for i in range(1, n):
        for j in range(1, m):
            b[i][j] = a[i][j] + b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1]

    for i in range(k):
        i1, j1, i2, j2 = map(int, input().split())
        if i1 == 1 and j1 == 1:
            print(b[i2 - 1][j2 - 1])
        elif i1 == 1 and j1 > 1:
            print(b[i2 - 1][j2 - 1] - b[i2 - 1][j1 - 2])
        elif i1 > 1 and j1 == 1:
            print(b[i2 - 1][j2 - 1] - b[i1 - 2][j2 - 1])
        else:
            m1 = b[i2 - 1][j2 - 1]
            m2 = b[i1 - 2][j2 - 1]
            m3 = b[i2 - 1][j1 - 2]
            m4 = b[i1 - 2][j1 - 2]
            print(m1 - m2 - m3 + m4)
    # for i in range(n):
    #     print(b[i])
