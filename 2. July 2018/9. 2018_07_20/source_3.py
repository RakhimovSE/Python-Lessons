#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # СЛОВАРЬ
    # Словарь обозначается фигурными скобками
    # объявление пустого словаря
    human = {}
    # инициализация словаря
    human = {
        'name': 'Ivan',
        'age': 26,
        'male': True,
        'city': 'Tyumen'
    }
    print('Исходный массив: ', human)
    # добавление элемента в словарь
    human['color'] = 'green'
    print('Добавили color: ', human)
    # изменение значение элемента
    human['city'] = 'Moscow'
    print('Изменили city: ', human)
    del human['age']
    print('Удалили age: ', human)

    # проверяем, есть ли ключ name в human
    if 'name' in human:
        print('В human есть ключ name')
    else:
        print('В human нет ключа name')

    print('Получаем массив ключей: ', list(human.keys()))
    print('Получаем массив значений: ', list(human.values()))
    print('Получаем кортеж (ключ, значение): ', list(human.items()))

    print()
    print('Перебор элементов словаря')
    for key in human:
        print('Ключ: %s, значение: %s' % (key, human[key]))

    print('\nПеребор элементов (2-ой вариант)')
    for key, value in human.items():
        print('Ключ: %s, значение: %s' % (key, value))
