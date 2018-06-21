if __name__ == '__main__':
    a = int(input())
    b = int(input())

    if a < b:
        for i in range(a, b + 1, +1):
            print(i)
    else:
        for i in range(a, b - 1, -1):
            print(i)