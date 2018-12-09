def ten_to_bin(x, n):
    return str(bin(x)[2:]).zfill(n)


def get_p(x):
    raw = ten_to_bin(x, n)
    p, w = 0, 0
    for i in range(len(raw)):
        if raw[i] == '1':
            w += a[i][0]
            p += a[i][1]
    return p if w <= W else 0


if __name__ == '__main__':
    n, W = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    result = 0
    max_i = -1
    max_p = 0
    for i in range(2 ** n):
        cur_p = get_p(i)
        if cur_p > max_p:
            max_i, max_p = i, cur_p

    if max_i == -1:
        print(0, 0)
        exit()
    raw = ten_to_bin(max_i, n)
    objs = []
    for i in range(len(raw)):
        if raw[i] == '1':
            objs.append(str(i + 1))
    print(len(objs), max_p)
    print(' '.join(objs))