#!/usr/bin/env python
# -*- coding: utf-8 -*-


# https://informatics.msk.ru/mod/statements/view3.php?id=26735&chapterid=113657#1

def f(st):
    result = st
    for i in range(len(st) - 1, -1, -1):
        result += ')' if st[i] == '(' else st[i]
    return result


if __name__ == '__main__':
    st = input()
    result = f(st)
    print(result)
