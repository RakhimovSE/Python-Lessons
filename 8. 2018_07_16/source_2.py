# Змейка и спираль


def fill_array(n, m, filler=0):
    result = []

    for i in range(n):
        result.append([])
        for j in range(m):
            result[i].append(filler)

    return result


# headers - необязательный параметр. Если его не указывать, по умолчанию он равен False
def print_array(arr, n, m, headers=False):
    row_st = '     '
    for j in range(m):
        row_st += '[%2d]' % j
    if headers == True:
        print(row_st)
    for i in range(n):
        # то же самое, что headers == True
        if headers:
            row_st = '[%3d]' % i
        else:
            row_st = ''
        for j in range(m):
            row_st += '%4d' % arr[i][j]
        print(row_st)


def snake(n, m):
    result = fill_array(n, m)

    k = 1

    xi, xj = 0, 0

    while xi < n - 1 or xj < m - 1:
        # идем в правый верхний угол
        while xi >= 0 and xj < m:
            result[xi][xj] = k
            k += 1
            xi -= 1
            xj += 1
        if xj == m:
            xi += 2
            xj = m - 1
        elif xi == -1:
            xi = 0

        # идем в левый нижний угол
        while xj >= 0 and xi < n:
            result[xi][xj] = k
            k += 1
            xi += 1
            xj -= 1
        if xi == n:
            xi = n - 1
            xj += 2
        elif xj == -1:
            xj = 0

    result[n - 1][m - 1] = n * m

    return result


def spiral(n, m):
    result = fill_array(n, m)

    # tr - top row
    # br - botton row
    # lc - left column
    # rc - right column
    tr, br = 0, n - 1
    lc, rc = 0, m - 1
    k = 1

    while True:
        if k > n * m:
            break
        for j in range(lc, rc + 1):
            result[tr][j] = k
            k += 1
        tr += 1

        if k > n * m:
            break
        for i in range(tr, br + 1):
            result[i][rc] = k
            k += 1
        rc -= 1

        if k > n * m:
            break
        for j in range(rc, lc - 1, -1):
            result[br][j] = k
            k += 1
        br -= 1

        if k > n * m:
            break
        for i in range(br, tr - 1, -1):
            result[i][lc] = k
            k += 1
        lc += 1

    return result


if __name__ == '__main__':
    n = int(input())
    m = int(input())

    print('Змейка')
    arr1 = snake(n, m)
    print_array(arr1, n, m)

    print('\nСпираль')

    arr2 = spiral(n, m)
    print_array(arr2, n, m)
