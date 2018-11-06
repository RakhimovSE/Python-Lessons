from queue import Queue

k = 0


def BFS(n, a, b, x, used):
    """

    :param n: кол-во вершин
    :param a: исходный граф
    :param b: новый граф, который мы строим по исходному
    :param x: номер вершины, от которой начинаем поиск
    :return:
    """
    global k
    q = Queue()
    q.put(x)
    used[x] = True
    while not q.empty():
        v = q.get()
        for j in range(n):
            if a[v][j] and not used[j]:
                k += 1
                b.append((v, j))
                q.put(j)
                used[j] = True


def func(n, m, a):
    used = [False for i in range(n)]
    result = []
    for i in range(n):
        if not used[i]:
            used[i] = True
            BFS(n, a, result, i, used)
    return result


if __name__ == '__main__':
    fin = open('roads.in', 'r')
    n, m = map(int, fin.readline().split())
    a = [[False for j in range(n)] for i in range(n)]
    for i in range(m):
        v1, v2 = map(int, fin.readline().split())
        a[v1 - 1][v2 - 1] = a[v2 - 1][v1 - 1] = True
    b = func(n, m, a)
    with open('roads.out', 'w') as f:
        print(k, file=f)
        for v1, v2 in b:
            print(v1 + 1, v2 + 1, file=f)
    fin.close()
