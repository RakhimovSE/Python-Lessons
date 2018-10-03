#!/usr/bin/env python
# -*- coding: utf-8 -*-

# кол-во повторений максимального числа


def maxn_rec():
    x = int(input())
    if x == 0:
        return 0, 0
    # m - максимальное число на данный момент
    # n - количество повторений максимального числа
    m, n = maxn_rec()
    if x > m:
        return x, 1
    if x == m:
        return m, n + 1
    return m, n


if __name__ == '__main__':
    m, n = maxn_rec()
    print('max:', m)
    print('count:', n)