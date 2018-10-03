#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Вывести через рекурсию числа от 1 до n

def f(n):
    if n > 1:
        f(n - 1)
    print(n)


def g(n):
    if n == 1:
        print(1)
    else:
        g(n - 1)
        print(n)


if __name__ == '__main__':
    n = int(input())
    f(n)
    print()
    g(n)