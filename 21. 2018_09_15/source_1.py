import random
from queue import Queue

def print_array(arr, n, m, headers=False):
    row_st = '     '
    for j in range(m):
        row_st += '[%2d]' % j
    if headers == True:
        print(row_st)
    for i in range(n):
        # то же самое, что headers == True
        if headers:
            row_st = '[%3d]' % i
        else:
            row_st = ''
        for j in range(m):
            row_st += '%4d' % arr[i][j]
        print(row_st)

def print_graph(arr, headers=False):
    #print_array(arr, len(arr), len(arr), headers)
    [print(''.join(map(str, row))) for row in arr]

def gen_graph(v, e):
    v1_v2 = []
    for i in range(v):
        for j in range(i + 1, v):
            v1_v2.append((i, j))
    edges = []
    for i in range(e):
        pair = random.choice(v1_v2)
        edges.append(pair)
        v1_v2.remove(pair)
    result = []
    for i in range(v):
        result.append([])
        for j in range(v):
            result[i].append(int((i, j) in edges or (j, i) in edges))
    return result

def DFS(arr, x, visited):
    visited[x] = True
    n = len(arr[x])
    print(x, end=' ')
    for j in range(n):
        if not visited[j] and arr[x][j] == 1:
            DFS(arr, j, visited)

def BFS(arr, x, visited):
    q = Queue()
    visited[x] = True
    # добавление x в конец очереди
    q.put(x)
    n = len(arr[x])
    while not q.empty():
        # получаем первый элемент и удаляем его из очереди
        i = q.get()
        print(i, end=' ')
        for j in range(n):
            if arr[i][j] == 1 and not visited[j]:
                q.put(j)
                visited[j] = True
    
def count_components(arr):
    n = len(arr)
    result = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            result += 1
            print('%d: ' % result, end='')
            BFS(arr, i, visited)
            print()
    return result


if __name__ == '__main__':
    v = int(input('Vertices count: '))
    e = int(input('Edges count: '))
    arr = gen_graph(v, e)
##    for i in range(n):
##        arr.append(list(map(int, input().split())))
    print_graph(arr)
    print(count_components(arr))
