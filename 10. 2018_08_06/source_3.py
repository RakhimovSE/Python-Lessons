#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Через datetime можем создать объект для работы с датами и временем
# Здесь используем для вычисления времени работы алгоритма
from datetime import datetime


def fibo(n):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, a + b
    return b


def fibo_rec(n):
    if n in (1, 2):
        return 1
    return fibo_rec(n - 1) + fibo_rec(n - 2)


if __name__ == '__main__':
    n = int(input())
    t1 = datetime.now()
    print('Число Фиббоначчи через цикл:', fibo(n))
    t2 = datetime.now()
    print('Время выполнения:', t2 - t1)
    print()

    print('Число Фиббоначчи через рекурсию:', fibo_rec(n))
    t3 = datetime.now()
    print('Время выполнения:', t3 - t2)
