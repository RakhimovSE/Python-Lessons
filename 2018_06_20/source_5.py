if __name__ == '__main__':
    a = int(input())
    b = int(input())

    sign = 1 if a < b else -1

    for i in range(a, b + sign, sign):
        print(i)