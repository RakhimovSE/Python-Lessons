from queue import Queue


def bfs(x):
    q = Queue()
    q.put(x)
    matrix[x] = 0
    while not q.empty():
        s = q.get()
        for i in range(n):
            if mas[s][i] != 0 and mas[s][i] < matrix[i]:
                q.put(i)
                matrix[i] = 1
                arr[i] = mas[s][i] + arr[s]


if __name__ == '__main__':
    fin = open("input.txt")
    fout = open("output.txt", "w")
    n = int(fin.readline())
    m = int(fin.readline())
    mas = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        a = list(map(int, fin.readline().split()))
        mas[a[0]][a[1]] = a[2]
    matrix = [100000000 for i in range(n)]
    arr = [0 for i in range(n)]
    x = int(fin.readline())
    bfs(x)
    print(arr)
    fout.close()
