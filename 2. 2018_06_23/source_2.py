#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Перевести все элементы в массива в числа
    # a = list(map(int, input().split()))
    # То же самое, что
    a = [int(i) for i in input().split()]
    x = int(input())
    b = 0
    while b < len(a) and a[b] >= x:
        b += 1
    print(b + 1)