#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def add_card(desk_cards, players_cards):
    card_index = random.randint(0, len(desk_cards) - 1)
    players_cards.append(desk_cards[card_index])
    desk_cards.pop(card_index)


def sum_cards(cards):
    card_sum = sum(cards)
    if card_sum > 21 and 11 in cards:
        ace_index = cards.index(11)
        cards[ace_index] = 1
        card_sum -= 10
    return card_sum


if __name__ == '__main__':
    cards = list(range(2, 12)) * 4
    my_cards = []
    for i in range(2):
        add_card(cards, my_cards)
    print("Сумма ваших карт = {card_sum}".format(card_sum=sum_cards(my_cards)))
    print(my_cards)
    print("Вы можете взять дополнительную карту")

    while True:
        p = input()
        if p == "Да":
            add_card(cards, my_cards)
            print("Сумма ваших карт = {card_sum}".format(card_sum=sum_cards(my_cards)))
            print(my_cards)
            if sum(my_cards) <= 21:
                print("Вы можете взять дополнительную карту")
            else:
                print("Вы проиграли!!!")
                break
        elif p == "Нет":
            print('Итоговая сумма: {card_sum}'.format(card_sum=sum_cards(my_cards)))
            break
        else:
            print("Неправильная команда. Введите 'Да' или 'Нет'")
