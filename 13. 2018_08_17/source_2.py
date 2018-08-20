#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Вводятся n, m и матрица n*m, состоящая из 0 и 1.
# 0 - вода
# 1 - суша
# Если несколько единиц соприкасаются (стоят рядом, но не по диагонали), то это считается одним островом
# Для того, чтобы работали цвета, надо установить termcolor (pip install termcolor)

import random

from termcolor import colored


def gen_map(n, m):
    result = []
    for i in range(n):
        result.append([])
        for j in range(m):
            result[i].append(random.randint(-1, 0))
    return result


def print_map(arr, n, m):
    global COLOR_IDS

    for i in range(n):
        st = ''
        for j in range(m):
            text = '%3d' % arr[i][j]
            if arr[i][j] == 0:
                st += colored(text, 'blue', attrs=['reverse'])
            elif arr[i][j] == -1:
                st += text
            else:
                st += colored(text, COLOR_IDS[arr[i][j] % len(COLOR_IDS)], attrs=['reverse'])
        print(st)


COLOR_IDS = ['red', 'green', 'yellow', 'grey', 'magenta', 'cyan', 'white']


def mark_island(arr, n, m, i, j, island_id):
    """

    :param arr: матрица (карта с водой и сушей)
    :param n: кол-во строк
    :param m: кол-во столбцов
    :param i: координата строки текущей ячейки
    :param j: координата столбца текущей ячейки
    :param island_id: номер текущего острова
    """
    arr[i][j] = island_id
    if i > 0 and arr[i - 1][j] == -1:
        mark_island(arr, n, m, i - 1, j, island_id)
    if j > 0 and arr[i][j - 1] == -1:
        mark_island(arr, n, m, i, j - 1, island_id)
    if i < n - 1 and arr[i + 1][j] == -1:
        mark_island(arr, n, m, i + 1, j, island_id)
    if j < m - 1 and arr[i][j + 1] == -1:
        mark_island(arr, n, m, i, j + 1, island_id)


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = gen_map(n, m)
    print_map(arr, n, m)
    print()
    island_id = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == -1:
                island_id += 1
                mark_island(arr, n, m, i, j, island_id)
    print_map(arr, n, m)
