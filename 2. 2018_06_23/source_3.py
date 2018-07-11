#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    if len(a) == 0:
        print(0)
    else:
        k = 1
        for i in range(1, len(a)):
            if a[i] != a[i - 1]:
                k += 1
        print(k)