if __name__ == '__main__':
    arr = [0] * 201
    result = ''
    n = int(input())
    mas = list(map(int, input().split()))
    for i in range(n):
        arr[mas[i] + 100] += 1
    for i in range(201):
        for j in range(arr[i]):
            result += '%d ' % (i - 100)
    print(result)
