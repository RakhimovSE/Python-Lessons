#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

if __name__ == '__main__':
    # генерируем 10 случайных чисел
    a = [random.randint(-1000, 1000) for i in range(10)]
    # переводим числа в строки
    a_str = [str(x) for x in a]
    print('Исходный массив целых чисел:')
    print(a)
    # сортируем массив чисел и выводим в консоль
    print('Отсортированный массив целых чисел')
    print(sorted(a))

    print()
    print('Исходный массив строк:')
    print(a_str)
    # сортируем массив строк и выводим в консоль
    print('Отсортированный массив строк')
    print(sorted(a_str))