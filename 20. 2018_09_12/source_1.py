import math

if __name__ == '__main__':
    a = [10, 50, 100, 500, 1000, 5000]
    b = list(map(int, input().split()))
    c = int(input())
    min_k = None
    summ = 0
    for i in range(len(b)):
        if min_k is None and b[i] > 0:
            min_k = a[i]
        summ += a[i] * b[i]
    # ищем все варианты в диапазоне от (summ - min_k; summ]
    min_kol = math.ceil((summ - min_k + 1) / c)
    max_kol = math.floor(summ / c)
    print(max_kol - min_kol + 1)
    print(' '.join(map(str, range(min_kol, max_kol + 1))))
