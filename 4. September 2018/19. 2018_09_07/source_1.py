n, k = None, None
a = None

def print_array(a):
    for row in a:
        for el in row:
            print(el, end=' ')
        print()

def read_data():
    global n, k, a
    with open('input.txt', 'r', encoding='utf-8') as f:
        raw_lines = f.read().split('\n')
##    То же самое, что:
##    f = open('input.txt', 'r', encoding='utf-8')
##    raw_lines = f.read().split('\n')
##    f.close()
##    минус последнего способа: надо явно прописывать команду закрытия файла
    a = []
    n, k = map(int, raw_lines[0].split())
    for i in range(n):
        a.append([0] * n)
    raw_lines = raw_lines[1:]
    for i in range(k):
        x1, x2 = map(int, raw_lines[i].split())
        a[x1 - 1][x2 - 1] = a[x2 - 1][x1 - 1] = 1

def write_data():
    global n, k, a
    with open('output.txt', 'w', encoding='utf-8') as f:
        st = ''
        for i in range(n):
            st += ' '.join(map(str, a[i])) + '\n'
        f.write(st)

read_data()
write_data()
