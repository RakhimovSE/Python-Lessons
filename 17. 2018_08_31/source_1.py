def bubble_sort(a, stop, start=0):
    for i in range(stop - 1, start, -1):
        for j in range(start, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    # считываем числа под номерами [0; n)
    k = int(input())
    bubble_sort(a, k, 0) # сортировка от [0; k)
    bubble_sort(a, n, k) # сортировка от [k; n)
    st = ' '.join(map(str, a))
    print(st)
