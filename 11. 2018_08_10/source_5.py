#!/usr/bin/env python
# -*- coding: utf-8 -*-

# подсчет кол-ва единиц
def uno():
    x = int(input())
    if x == 1:
        return uno() + 1
    x2 = int(input())
    if x2 == 0:
        return 0
    return x2 + uno()


if __name__ == '__main__':
    print(uno())
