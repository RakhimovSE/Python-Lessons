#!/usr/bin/env python
# -*- coding: utf-8 -*-


# среднее арифметическое через рекурсию


def avg(s, n):
    x = int(input())
    if x == 0:
        return s, n

    return avg(s + x, n + 1)


if __name__ == '__main__':
    s, n = avg(0, 0)
    print(s / n)
