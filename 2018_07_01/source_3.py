#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

if __name__ == '__main__':
    n, m = int(input()), int(input())
    arr = []
    row_st = '     '
    for j in range(m):
        row_st += '[%2d]' % j
    print(row_st)
    for i in range(n):
        arr.append([])
        row_st = '[%3d]' % i
        for j in range(m):
            arr[i].append(random.randint(-20, 20))
            row_st += '%4d' % arr[i][j]
        print(row_st)

