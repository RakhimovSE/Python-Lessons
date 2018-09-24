import math


def f(x):
    return x * x


def bin_search(c):
    E = 10 ** (-7)
    x = None
    start,end = 0, 10 ** 5
    while (end - start) > E:
        x = (start + end) / 2
        if f(x) <= c:
            start = x
        else:
            end = x
    return x


if __name__ == '__main__':
    c = float(input())
    res = bin_search(c)
    print(res)
    #print('%.6f' % bin_search(c))
