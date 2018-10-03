#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def generate_array(n, m):
    result = []
    for i in range(n):
        result.append([])
        for j in range(m):
            result[i].append(random.randint(0, 1))
    return result


def print_array(arr):
    for row in arr:
        st = ''
        for el in row:
            st += str(el)
        print(st)


if __name__ == '__main__':
    n, m = int(input()), int(input())

    arr = generate_array(n, m)
    print_array(arr)
