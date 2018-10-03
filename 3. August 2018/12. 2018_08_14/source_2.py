#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://informatics.msk.ru/mod/statements/view3.php?id=26735&chapterid=113659#1

def read_messages(n):
    # result хранит связи между сообщениями. Номер элемента = номер сообщения, значение - массив номеров дочерних элементов
    result = [[] for i in range(1000001)]
    for i in range(n):
        x, y = map(int, input().split())
        result[y].append(x)
    return result

def remove_msg_count(messages, k):
    result = 1
    for child_msg in messages[k]:
        result += remove_msg_count(messages, child_msg)
    return result

def bfs(messages, k):
    result = 0
    q = [k]
    while len(q) > 0:
        result += 1
        q.extend(messages[q[0]])
        q.pop(0)
    return result


if __name__ == '__main__':
    n = int(input())
    messages = read_messages(n)
    k = int(input())
    # print(remove_msg_count(messages, k))
    print(bfs(messages, k))