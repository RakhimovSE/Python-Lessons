def ok(a: list):
    a.sort(reverse=True)
    sa = [0 for x in a]
    sa[-1] = a[-1]
    for i in range(len(a) - 2, -1, -1):
        sa[i] = a[i] + sa[i + 1]
    for i in range(len(a) - 1):
        if a[i] < sa[i + 1]:
            return False
    return True


if __name__ == '__main__':
    with open('stack.in', 'r') as f:
        rows = f.read().splitlines()
        n, k = map(int, rows[0].split())
        rows = rows[1:]
    fout = open('stack.out', 'w')
    for i in range(n):
        a = list(map(int, rows[i].split()))
        print('yes' if ok(a) else 'no', file=fout)
    fout.close()