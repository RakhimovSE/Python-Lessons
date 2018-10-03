import random
from time import sleep


# итеративный алгоритм бинарного поиска (через цикл)
def bin_search_iter(mas, l, r, k):
    # l - индекс левой границы
    # r - индекс правой границы
    # m - индекс среднего элемента
    while l < r:
        m = (l + r) // 2
        if k == mas[m]:
            return True
        if k < mas[m]:
            r = m - 1
        else:
            l = m + 1
    return k == mas[l]


# рекурсивный алгоритм бинарного поиска
def bin_search_rec(mas, l, r, k):
    m = (l + r) // 2
    if l == r:
        return k == mas[l]
    if k == mas[m]:
        return True
    if k < mas[m]:
        return bin_search_rec(mas, l, m - 1, k)
    return bin_search_rec(mas, m + 1, r, k)


if __name__ == '__main__':
    n = int(input())
    mas = []
    for i in range(n):
        mas.append(random.randint(-100,100))
    mas.sort()
    print(mas)
    k = int(input())
    if n == 0:
        print(False)
    else:
        print('Итеративный:', bin_search_iter(mas, 0, n - 1, k))
        print('Рекурсивный:', bin_search_rec(mas, 0, n - 1, k))
