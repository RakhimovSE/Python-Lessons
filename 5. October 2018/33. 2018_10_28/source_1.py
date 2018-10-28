def amount(p, digit_count):
    """
    Вычисляет кол-во i-значных чисел в n-ичной системе счисления
    :param p: Система счисления
    :param digit_count: Кол-во знаков числа
    :return:
    """
    return (p - 1) * p ** (digit_count - 1)


def to_base(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_base(n // base, base) + convert_string[n % base]


def func(p, n):
    digit_count = 1
    digit_sum = 0
    while True:
        cur_count = amount(p, digit_count) * digit_count
        if digit_sum + cur_count >= n:
            break
        digit_sum += cur_count
        digit_count += 1
    nums_before = (n - digit_sum - 1) // digit_count
    first_num10 = int('1' + '0' * (digit_count - 1), p)
    num_search = to_base(first_num10 + nums_before, p)
    digit_index = n - digit_sum - nums_before * digit_count - 1
    return num_search[digit_index]


if __name__ == '__main__':
    with open('input.txt', 'r', encoding='UTF-8') as f:
        p, n = map(int, f.read().split())

    result = func(p, n)
    with open('output.txt', 'w', encoding='UTF-8') as f:
        f.write(result)
