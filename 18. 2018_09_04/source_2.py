import random
from time import sleep


# Если фунция возвращает True, то мы можем разместить всех коров на расстоянии
# не меньше x. Если False, то не можем
def max_cow_count(mas, n, x):
    last_idx = 0
    cow_count = 1
    for i in range(n):
        if mas[i] - mas[last_idx] >= x:
            last_idx = i
            cow_count += 1
    return cow_count


# итеративный алгоритм бинарного поиска (через цикл)
def bin_search(mas, n, k):
    # l - индекс левой границы
    # r - индекс правой границы
    # m - индекс среднего элемента
    l = mas[0]
    r = mas[-1] - mas[0]
    while l < r:
        x = (l + r) // 2
        k = max_cow_count(mas, n, x)
        if k > n:
            r = m - 1
        else:
            l = m + 1
    k = (l // w) * (l // h)
    if k >= n:
        return l
    else:
        return l + 1


if __name__ == '__main__':
    w, h, n = map(int, input().split())
    print(bin_search(w, h, n))
