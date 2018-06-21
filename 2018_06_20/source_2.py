# Проверка: если текущий файл - главный (тот, который мы запустили), то выполнить код
if __name__ == '__main__':
    days = [20, 16, 18, 10, 6]

    days.append(15)
    days.append(21)

    print('Original array: ', days)

    s = 0

    for i in range(0, len(days)):
        s += days[i]

    print('Changed array: ', days)
    print('Array sum: ', s)
    print('Average: ', s / len(days))
