if __name__ == '__main__':
    s = input()
    d = {}
    b = ''
    j = 0
    for el in s:
        a = el + '%d' % j
        if not a in d:
            d[a] = 1
        elif a in d and a != b:
            j += 1
            a = el + '%d' % j
            d[el + '%d' % j] = 1
        else:
            d[a] += 1
        b = a
    answer = ''
    for el in d:
        if d[el] > 1:
            answer += el[0]
            answer += str(d[el])
        elif d[el] == 1:
            answer += el[0]
    print(answer)
