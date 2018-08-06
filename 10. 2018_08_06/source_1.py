#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fact(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result


def fact_rec(n):
    if n == 1:
        return 1
    return n * fact_rec(n - 1)


if __name__ == '__main__':
    n = int(input())
    print('Факториал через цикл', fact(n))
    print('Факториал через рекурсию', fact_rec(n))
