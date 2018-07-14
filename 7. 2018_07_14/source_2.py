import random

# Виды циклов

if __name__ == '__main__':
    arr = [random.randint(-10, 10) for i in range(10)]
    print(arr)
    print()

    print('Цикл со счетчиком')
    for i in range(len(arr)):
        print('arr[%d] = %d' % (i, arr[i]))
    print()

    print('Цикл с перебором элементов')
    # Каждый элемент массива по порядку записываем в переменную x
    # Минус: мы не знаем номер элемента
    for x in arr:
        print(x)

    print()
    print('Цикл со счетчиком и перебором элементов')
    print(list(enumerate(arr)))
    for i, x in enumerate(arr):
        print('arr[%d] = %d' % (i, x))
