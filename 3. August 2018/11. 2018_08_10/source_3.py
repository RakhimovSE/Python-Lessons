#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2-ое максимальное число через рекурсию


def max2_rec():
    x = int(input())
    if x == 0:
        return 0, 0
    m1, m2 = max2_rec()
    if x >= m1:
        return x, m1
    if x >= m2:
        return m1, x
    return m1, m2


if __name__ == '__main__':
    m1, m2 = max2_rec()
    print('max1:', m1)
    print('max2:', m2)