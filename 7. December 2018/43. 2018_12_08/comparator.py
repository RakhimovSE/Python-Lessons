import random
from functools import cmp_to_key


def my_cmp(a, b):
    '''
    Функция-компаратор. a и b - какие-то 2 числа из массива.
    Если функция возвращает -1, то они стоят на своих местах (a должно быть слева, b должно быть справа)
    Если функция возвращает 1, то их надо поменять местами
    Если функция возвращает 0, то переменные равны (не обязательно использовать)
    '''
    if a > b:
        return 1
    return -1


def champion_cmp(a, b):
    # a, b - массивы из 2 элементов (0-ой элемент - id, 1-ый элемент - кол-во баллов)
    # если у a больше баллов, чем у b, он должен быть раньше, и наоборот
    # если кол-во баллов а = кол-во баллов b, первым идет участник с наименьшим id
    if a[1] > b[1]:
        return -1
    if a[1] < b[1]:
        return 1
    if a[0] < b[0]:
        return -1
    return 1


if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append([x, y])
    a.sort(key=cmp_to_key(champion_cmp))
    for x in a:
        print(x[0], x[1])