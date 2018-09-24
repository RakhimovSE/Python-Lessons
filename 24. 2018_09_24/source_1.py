# если возвращает 1 - кузнечик выше прямой
# если 0 - на прямой
# если -1 - ниже прямой
def f(p1, p2, p):
    a = p[1] - (p[0] - p1[0]) * (p2[1] - p1[1]) / (p2[0] - p1[0]) - p1[1]
    return a

if __name__ == '__main__':
    n, d = map(int, input().split())
    p1 = (0, d)
    p2 = (d, 0)
    p3 = (n, n - d)
    p4 = (n - d, n)
    m = int(input())

    for i in range(m):
        p = tuple(map(int, input().split()))
        if f(p1, p2, p) >= 0 and f(p2, p3, p) >= 0 and f(p3, p4, p) <= 0 and f(p1, p4, p) <= 0:
            print('YES')
        else:
            print('NO')
