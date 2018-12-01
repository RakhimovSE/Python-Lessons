from queue import Queue


def DFS(x):
    for j in range(n):
        if a[x][j] == True:
            if used[j] != 0:
                if used[x] == used[j]:
                    print(-1)
                    exit()
                continue
            if used[x] == 1:
                used[j] = 2
            else:
                used[j] = 1
            DFS(j)


def BFS(x):
    used[x] = 1
    q = Queue()
    q.put(x)
    while not q.empty():
        v = q.get()
        for j in range(n):
            if a[v][j] == True:
                if used[j] != 0:
                    if used[v] == used[j]:
                        print(-1)
                        exit()
                    continue
                if used[v] == 1:
                    used[j] = 2
                else:
                    used[j] = 1
                q.put(j)


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [[False for j in range(n)] for i in range(n)]
    used = [0 for i in range(n)]
    for i in range(m):
        v1, v2 = map(int, input().split())
        v1, v2 = v1 - 1, v2 - 1
        a[v1][v2] = a[v2][v1] = True
    result = []
    for i in range(n):
        if used[i] == 0:
            used[i] = 1
            DFS(i)
            result.append(str(i + 1))
    print(len(result))
    print(' '.join(result))
