#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def read_array(n, m):
    arr = []
    for i in range(n):
        arr.append([])
        for j in range(m):
            arr[i].append(random.randint(-20, 20))
    return arr


# headers - необязательный параметр. Если его не указывать, по умолчанию он равен False
def print_array(arr, n, m, headers=False):
    row_st = '     '
    for j in range(m):
        row_st += '[%2d]' % j
    if headers == True:
        print(row_st)
    for i in range(n):
        # то же самое, что headers == True
        if headers:
            row_st = '[%3d]' % i
        else:
            row_st = ''
        for j in range(m):
            row_st += '%4d' % arr[i][j]
        print(row_st)


if __name__ == '__main__':
    n, m = int(input()), int(input())
    arr = read_array(n, m)
    print_array(arr, n, m)
