def dijkstra(mas, n, start):
    result = [100000000 for i in range(n)]
    used = [False for i in range(n)]
    result[start] = 0
    for i in range(n):
        x = None
        for j in range(n):
            if not used[j] and (x is None or result[j] < result[x]):
                x = j
        used[x] = True
        for j in range(n):
            # result[x] - кратчайшее расстояние до текущей наименьшая вершины
            # mas[x][j] - расстояние от текущей наименьшей до соседней с ней
            # result[j] - кратчайшее расстояние до соседней, найденное на данный момент
            # mas[x][j] != 0 означает, что между вершинами x и j есть ребро
            if mas[x][j] != 0 and result[x] + mas[x][j] < result[j]:
                result[j] = result[x] + mas[x][j]
        print(i, result, used)
    return result


if __name__ == '__main__':
    fin = open("input.txt")
    n = int(fin.readline())
    m = int(fin.readline())
    mas = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        a = list(map(int, fin.readline().split()))
        mas[a[0]][a[1]] = a[2]

    x = int(fin.readline())
    arr = dijkstra(mas, n, x)
    print(arr)
