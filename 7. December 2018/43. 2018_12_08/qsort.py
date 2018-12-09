import random


def qsort(a, l, r):
    i, j = l, r
    x = a[(l + r) // 2]
    while i <= j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if l < j:
        qsort(a, l, j)
    if i < r:
        qsort(a, i, r)


if __name__ == '__main__':
    n = int(input())
    a = [random.randint(-1000, 1000) for i in range(n)]
    print('Исходный массив:', a)
    qsort(a, 0, len(a) - 1)
    print('Отсортированный массив:', a)