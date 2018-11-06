def func(n, m):
    if n == 1:
        return 1
    result = 0
    for x in range(min(n, m), 1, -1):
        if n % x == 0:
            result += func(n // x, x)
    return result


if __name__ == '__main__':
    with open('factor.in', 'r') as f:
        n, m = map(int, f.read().split())
    with open('factor.out', 'w') as f:
        print(func(n, m), file=f)