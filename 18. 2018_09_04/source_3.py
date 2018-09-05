import math


def f(x):
    return x ** 2 + math.sqrt(x)


# итеративный алгоритм бинарного поиска (через цикл)
def bin_search(C):
    # l - индекс левой границы
    # r - индекс правой границы
    # m - индекс среднего элемента
    l = 0.0
    r = 10.0 ** 5
    e = 10.0 ** (-7)
    x = 0.0
    while (r - l) > e:
        x = (l + r) / 2
        y = f(x)
        if y > C:
            r = x
        else:
            l = x
    return x

if __name__ == '__main__':
    C = float(input())
    print(bin_search(C))
