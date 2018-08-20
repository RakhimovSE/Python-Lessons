#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_messages(n):
    # result хранит связи между сообщениями. Номер элемента = номер сообщения, значение - массив номеров дочерних элементов
    result = [[] for i in range(1000001)]
    for i in range(n):
        x, y = map(int, input().split())
        result[y].append(x)
    return result


def get_max_msg(messages, msg_id, msgs_before):
    if len(messages[msg_id]) == 0:
        return msgs_before + 1

    result = 0
    for child_id in messages[msg_id]:
        result = max(result, get_max_msg(messages, child_id, msgs_before + 1))
    return result


if __name__ == '__main__':
    n = int(input())
    messages = read_messages(n)
    result = 0
    for root_id in messages[0]:
        result = max(result, get_max_msg(messages, root_id, 0))
    print(result)
