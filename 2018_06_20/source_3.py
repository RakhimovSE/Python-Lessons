import random


if __name__ == '__main__':
    n = int(input('Type element count: '))

    arr = []

    for i in range(0, n):
        arr.append(random.randint(-1000, 1000))

    print(arr)