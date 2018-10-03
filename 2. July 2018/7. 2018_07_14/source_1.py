import random, math


# Считывание массива
def read_array(n, rand_range=30):
    result = []
    for i in range(n):
        result.append(random.randint(-rand_range, rand_range))
    return result


# Медиана
def median(mass):
    mass = sorted(mass)
    if n % 2 != 0:
        res = n // 2
        return mass[res]
    else:
        res = n // 2 - 1
        return (mass[res] + mass[res + 1]) / 2


# Стандартное отклонение (standard deviation)
def deviation(mass):
    n = len(mass)
    avg = sum(mass) / n
    return math.sqrt(sum([(x - avg) ** 2 for x in mass]) / n)


if __name__ == '__main__':
    n = int(input())
    arr = read_array(n)
    print(arr)
    print('Медиана: ', median(arr))
    print('Стандартное отклонение: %.2f' % deviation(arr))
