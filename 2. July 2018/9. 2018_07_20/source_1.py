#!/usr/bin/env python
# -*- coding: utf-8 -*-


def print_array(arr, n, m, headers=True):
    row_st = '     '
    for j in range(1, m + 1):
        row_st += '[%2d]' % j
    if headers == True:
        print(row_st)
    for i in range(1, n + 1):
        # то же самое, что headers == True
        if headers:
            row_st = '[%3d]' % i
        else:
            row_st = ''
        for j in range(1, m + 1):
            row_st += '%4d' % arr[i][j]
        print(row_st)


def fill_array(n, m):
    arr = []
    for i in range(n + 1):
        arr.append([])
        for j in range(m + 1):
            arr[i].append(j * i)
    return arr


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    arr = fill_array(n, m)
    print_array(arr, n, m)
