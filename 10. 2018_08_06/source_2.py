#!/usr/bin/env python
# -*- coding: utf-8 -*-

def F(n):
    if n > 2:
        return F(n - 1) + G(n - 2)
    else:
        return n + 1


def G(n):
    if n > 2:
        return G(n - 1) + F(n - 2)
    else:
        return n


if __name__ == '__main__':
    print(G(7))