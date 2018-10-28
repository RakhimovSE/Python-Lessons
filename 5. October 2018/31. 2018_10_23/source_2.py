# Числа Фибоначчи определяются следующим образом: F1 = 1, F2 = 2, а для n > 2
# выполнено Fn = Fn−2+Fn−1. Таким образом, начало последовательности чисел Фибоначчи
# выглядит так 1, 2, 3, 5, 8, 13, 21, . . ..
# Вам заданы числа n и k. Требуется найти все способы представить число n в виде суммы
# неубывающих чисел Фибоначчи, причем кажое число разрешается использовать не более
# k раз.
from datetime import datetime


fibo = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# fibo = [89, 55, 34, 21, 13, 8, 5, 3, 2, 1]


def f(word, n, last_fibo_idx, repeats):
    if n == 0:
        return [word]
    result = []
    for i in range(last_fibo_idx, -1, -1):
        if n >= fibo[i] and repeats[i] > 0:
            repeats[i] -= 1
            result.extend(f(chr(ord('A') + i) + word, n - fibo[i], i, repeats))
            repeats[i] += 1
    return result


def word_to_sum(word):
    def letter_to_fibo(ch):
        # ord - функция, которая переводит символ в код в ASCII
        return fibo[ord(ch) - ord('A')]

    a = map(letter_to_fibo, word)
    return '+'.join(map(str, a))


def print_time(message=''):
    global start
    now = datetime.now()
    print(message, now - start)
    start = now


if __name__ == '__main__':
    n, k = int(input()), int(input())
    start = datetime.now()
    repeats = [k for i in range(10)]
    raw = f('', n, len(fibo) - 1, repeats)
    print_time('Посчитали все варианты')
    raw = sorted(raw)
    print_time('Отсортировали')
    with open('output.txt', 'w', encoding='utf-8') as f:
        for word in raw:
            f.write(word_to_sum(word) + '\n')
    print_time('Записали в файл')