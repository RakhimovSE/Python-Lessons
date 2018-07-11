#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = [int(x) for x in input().split()]
    a = sorted(a)
    # если писать элемент с отрицательным индексом, будет браться элемент с конца
    print(a[-2])
    # то же самое, что
    # print(a[len(a) - 2])
