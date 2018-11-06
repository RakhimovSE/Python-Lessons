# если операция False - либо вычитание знаменателя из числителя (если преобразуем исходную дробь к 1/1),
# либо прибавление (если преобразуем результат к 1/1)
# True - переворот дроби
from datetime import datetime


def num_to_word(arr: list, reversed=False):
    result = ''
    if reversed:
        arr.reverse()
    for oper in arr:
        if oper == False:
            if reversed:
                result += 'A'
            else:
                result += 'B'
        else:
            result += 'C'
    return result


def get_operations(a, b):
    result = []
    while not (a == 1 and b == 1):
        if a < b:
            result.append(True)
            a, b = b, a
        else:
            result.append(False)
            a -= b
    return result


if __name__ == '__main__':
    start = datetime.now()
    with open('fractions.in', 'r', encoding='UTF-8') as f:
        rows = f.read().splitlines()
        a, b = map(int, rows[0].split())
        c, d = map(int, rows[1].split())
    arr1 = get_operations(a, b)
    arr2 = get_operations(c, d)
    result = num_to_word(arr1) + num_to_word(arr2, True)
    n = len(result)
    with open('fractions.out', 'w', encoding='UTF-8') as f:
        f.write('%d\n%s' % (n, result))
    end = datetime.now()
    print(end - start)
