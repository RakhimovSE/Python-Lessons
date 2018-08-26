import random

def randword(n=5):
    result = ''
    for i in range(n):
        result += chr(random.randint(ord('a'), ord('z')))
    return result

# ПУЗЫРЬКОВАЯ СОРТИРОВКА
# i - номер числа, до которого надо сравнивать соседние числа
# изначально i - последнее число, и мы проверяем все числа
# после первого прохода по циклу в конец "всплыл" наибольший элемент
# потом i - предпоследнее число, и мы сравниваем все соседние числа до предпоследнего и т.д.
def bubble_sort(a, n):
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

# СОРТИРОВКА ВСТАВКАМИ
def insertion_sort(a, n):
    for i in range(n):
        x = a[i]
        j = i
        while j > 0 and a[j - 1] > x:
            a[j] = a[j - 1]
            j -= 1
        a[j] = x

# ГНОМЬЯ СОРТИРОВКА
def gnome_sort(a, n):
    for i in range(n):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1

if __name__ == '__main__':
    n = int(input())
    a = [random.randint(-99, 99) for i in range(n)]
    # a = [randword() for i in range(n)]
    print(a)
    # bubble_sort(a, n)
    # insertion_sort(a, n)
    gnome_sort(a, n)
    print(a)
