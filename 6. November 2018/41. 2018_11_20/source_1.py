import random


def get_h():
    return random.randint(0, n - 1)


def ins_el(a, el=1):
    h, k = get_h(), 0
    while a[(h + k) % n] is not None:
        k += 1
    a[(h + k) % n] = el
    return k


def test(n, m):
    a = [None for i in range(n)]
    result = 0
    for i in range(m):
        result += ins_el(a, 1)
    return result


if __name__ == '__main__':
    n, m = map(int, input().split())
    s, t = 0, 10 ** 5
    for i in range(t):
        s += test(n, m)
        # print('%i. Кол-во коллизий: %d' % (i + 1, test(n, m)))
    print(s / t)
