#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Треугольная последовательность

# k - текущее число, которое будем выводить
# l - кол-во оставшихся чисел для вывода
def triseq(k, l):
    for i in range(min(k, l)):
        print(k)
    if l > k:
        triseq(k + 1, l - k)


if __name__ == '__main__':
    n = int(input())
    triseq(1, n)