#!/usr/bin/env python
# -*- coding: utf-8 -*-

# максимальное число через рекурсию


def max_rec(m):
    x = int(input())
    if x == 0:
        return m
    if x > m:
        return max_rec(x)
    return max_rec(m)


if __name__ == '__main__':
    print(max_rec(0))