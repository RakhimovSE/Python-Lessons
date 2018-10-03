#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://informatics.msk.ru/mod/statements/view3.php?id=26736&chapterid=113660#1

def read_messages(n):
    # result хранит связи между сообщениями. Номер элемента = номер сообщения, значение - номер родительского сообщения
    result = [None] * 1000001
    for i in range(n):
        x, y = map(int, input().split())
        result[x] = y
    return result


def get_root(messages, a):
    current_root = a
    while messages[current_root] != 0:
        current_root = messages[current_root]
    return current_root


if __name__ == '__main__':
    n = int(input())
    messages = read_messages(n)
    a = int(input())
    print(get_root(messages, a))