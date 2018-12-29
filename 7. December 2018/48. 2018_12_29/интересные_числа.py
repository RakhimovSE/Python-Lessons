def get_l(R):
    for i in range(1, len(R)):
        if R[i - 1] > R[i]:
            return i
    return len(R)


def f(R: str):
    k = len(R)
    d = [[0 for j in range(10)] for i in range(k + 2)]
    for i in range(1, k + 1):
        l = get_l(R[:i - 1])
        for j in range(int(R[l - 1]), int(R[l])):
            d[l + 1][j] = 1
    for i in range(k + 1):
        for j in range(10):
            print(d[i][j], end='')
        print()


if __name__ == '__main__':
    # L = input()
    # R = input()
    f('100')
