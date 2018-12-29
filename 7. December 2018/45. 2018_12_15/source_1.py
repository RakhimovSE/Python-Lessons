from queue import Queue


def get_component(idx):
    used = [False for i in range(n)]
    q = Queue()
    q.put(idx)
    while not q.empty():
        x = q.get()
        used[x] = True
        for i in range(n):
            if not used[i] and (d[i] % d[x] == 0 or d[x] % d[i] == 0):
                q.put(i)
    result = []
    for i in range(n):
        if used[i]:
            result.append(i)
    return result


def sort_component(d, comp):
    for i in range(len(comp)):
        for j in range(len(comp) - 1, i - 1, -1):
            if d[comp[i]] > d[comp[j]]:
                d[comp[i]], d[comp[j]] = d[comp[j]], d[comp[i]]


if __name__ == '__main__':
    n = int(input())
    d = list(map(int, input().split()))
    d_original = d.copy()
    d_sorted = sorted(d)
    m = {x: [] for x in d}
    if d == d_sorted:
        print(0)
        exit()
    used = [False for i in range(n)]
    for i in range(n):
        if not used[i]:
            comp = get_component(i)
            # указываем в матрице смежности связь между вершинами компоненты связности
            for j in range(len(comp)):
                for k in range(j + 1, len(comp)):
                    k1, k2 = d[comp[j]], d[comp[k]]
                    if k1 % k2 == 0 or k2 % k1 == 0:
                        m[k1].append(k2)
                        m[k2].append(k1)
            sort_component(d, comp)
            for j in range(len(comp)):
                used[comp[j]] = True

    if d != d_sorted:
        print(-1)
        exit()
