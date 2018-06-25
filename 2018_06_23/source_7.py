#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = input().split()
    b = int(input())
    for i in range(b + 1, len(a)):
        a[i - 1] = a[i]
    a.pop()
    print(' '.join(a))
