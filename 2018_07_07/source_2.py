#!/usr/bin/env python
# -*- coding: utf-8 -*-

def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def nok(a, b):
    return a * b / nod(a, b)


def print_result(a, b):
    print('НОД(%d; %d) = %d' % (a, b, nod(a, b)))
    print('НОК(%d; %d) = %d' % (a, b, nok(a, b)))


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print_result(a, b)
