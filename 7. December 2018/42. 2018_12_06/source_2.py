if __name__ == '__main__':
    a = [i ** 3 for i in range(1, 101)]
    n = int(input())
    f = [101 for i in range(n + 1)]
    f[0] = 0
    for i in range(n + 1):
        for j in range(len(a)):
            if i < a[j]:
                break
            if f[i - a[j]] + 1 < f[i]:
                f[i] = f[i - a[j]] + 1
    print(f[n])
