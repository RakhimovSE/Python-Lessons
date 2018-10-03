#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_value_from_tuple(letter_tuple):
    return letter_tuple[1]

if __name__ == '__main__':
    st = input()
    letters = {}
    for ch in st:
        if ch in letters:
            letters[ch] += 1

        else:
            letters[ch] = 1
    # for letter, count in letters.items():
    #     print('\'%s\': %s' % (letter, count))

    # lambda - анонимная функция (лямбда-выражение)
    # callback-функция
    letters_ordered = sorted(letters.items(), key=get_value_from_tuple, reverse=True)
    print(letters_ordered)
    for letter, count in letters_ordered:
        print('\'%s\': %s' % (letter, count))
