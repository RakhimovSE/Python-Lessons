#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = input().split()
    for i in range(1, len(a), 2):
        # Поменять значения местами
        a[i - 1], a[i] = a[i], a[i - 1]
        # То же самое, что
        # x = a[i - 1]
        # a[i - 1] = a[i]
        # a[i] = x
    print(' '.join(a))
