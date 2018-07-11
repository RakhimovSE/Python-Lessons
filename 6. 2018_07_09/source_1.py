#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = input().split()
    a, b = int(a[0]), int(a[1])

    # время на обувание 39 левых и 39 правых ног
    x = 39 + 39 * 2

    # оставшееся кол-во тапок для левой и правой ног
    a, b = a - 39, b - 39

    if a > b:
        x += 1 + (a - 1) * 2 + 1
    else:
        x += b * 2 + 1
    print(x)