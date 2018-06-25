#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = input().split()
    min_i, max_i = 0, 0
    for i in range(len(a)):
        if int(a[i]) > int(a[max_i]):
            max_i = i
        if int(a[i]) < int(a[min_i]):
            min_i = i
    a[min_i], a[max_i] = a[max_i], a[min_i]
    print(' '.join(a))
