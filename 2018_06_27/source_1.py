#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [int(i / 100) for i in range(-1000, 1001)]

    y = [1 / i if i != 0 else None for i in x]
    plt.plot(x, y)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()