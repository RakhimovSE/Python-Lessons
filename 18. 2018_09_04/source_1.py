# итеративный алгоритм бинарного поиска (через цикл)
def bin_search(w, h, n):
    # l - индекс левой границы
    # r - индекс правой границы
    # m - индекс среднего элемента
    l = 0
    r = max(w * n, h * n)
    while l < r:
        m = (l + r) // 2
        # k - максимальное количество дипломов, которое можно
        # разместить на доске длиной m
        k = (m // w) * (m // h)
        # Если k (макс. кол-во дипломов) = n
        if k == n:
            return m
        if k > n:
            r = m - 1
        else:
            l = m + 1
    k = (l // w) * (l // h)
    if k >= n:
        return l
    else:
        return l + 1


if __name__ == '__main__':
    w, h, n = map(int, input().split())
    print(bin_search(w, h, n))
