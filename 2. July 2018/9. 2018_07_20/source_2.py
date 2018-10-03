#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    words = ['Hello', 'world', 'Ivan']
    # поиск строковой переменной в массиве
    if 'Hello' in words:
        print('Hello есть')
    else:
        print('Hello нет')
    arr = list(range(100))
    # поиск числовой переменной в массиве
    # проверка, есть ли число 21 в массиве
    if 21 in arr:
        print('21 есть в массиве')
    else:
        print('21 нет в массиве')

    # поиск подстроки в строке
    st = 'Hello world'
    if 'world' in st:
        print('world есть в строке st')
    else:
        print('world нет в строке st')