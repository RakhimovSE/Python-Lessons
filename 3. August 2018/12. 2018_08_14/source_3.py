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


def is_a_root_b(messages, a, b):
    current_root = b
    while current_root is not None:
        if current_root == a:
            return True
        current_root = messages[current_root]
    return False


if __name__ == '__main__':
    n = int(input())
    messages = read_messages(n)
    a, b = map(int, input().split())
    print('YES' if is_a_root_b(messages, a, b) else 'NO')
    # if is_a_root_b(messages, a, b):
    #     print('YES')
    # else:
    #     print('NO')
