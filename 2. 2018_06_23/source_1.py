#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задание "Поиск максимального": http://pythontutor.ru/lessons/lists/problems/maximal_element/
if __name__ == '__main__':
    a = input().split()
    # c - номер максимального элемента
    c = 0
    for i in range(0, len(a)):
        if int(a[i]) > int(a[c]):
            c = i

    print(a[c], c)