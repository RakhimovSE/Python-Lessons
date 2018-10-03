#!/usr/bin/env python
# -*- coding: utf-8 -*-

# s - сумма цифр предыдущих разрядов числа
# a - номер текущего разряда
# k - кол-во разрядов в числе
# d - искомая сумма
def f(s, a, k, d):
    # если текущий разряд - последний
    if a == k:
        return d <= s + 9
        # то же самое. Когда переводим bool в int: True = 1, False = 0
        # if d <= s + 9:
        #     return 1
        # else:
        #     return 0
    result = 0
    start = 1 if a == 1 else 0
    stop = min(10, d - s + 1)
    for i in range(start, stop):
        result += f(s + i, a + 1, k, d)
    return result


if __name__ == '__main__':
    k, d = int(input()), int(input())
    print(f(0, 1, k, d))
