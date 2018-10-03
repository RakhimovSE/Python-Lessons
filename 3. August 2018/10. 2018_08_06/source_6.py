#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Вывести через рекурсию числа от a до b

def f(a, b):
    if a < b:
        f(a, b - 1)
    elif a > b:
        f(a, b + 1)
    print(b)


if __name__ == '__main__':
    a, b = int(input()), int(input())
    f(a, b)
