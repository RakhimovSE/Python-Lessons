# Проверка: если текущий файл - главный (тот, который мы запустили), то выполнить код
if __name__ == '__main__':
    days = [20, 16, 18, 10]

    days.append(15)
    days.append(21)

    print('Original array: ', days)

    s = 0
    b = 0

    for i in range(0, 6):
        s += days[i]
        b += 1

    print('Changed array: ', days)
    print('Array sum: ', s)
    print('Average: ', s / b)
