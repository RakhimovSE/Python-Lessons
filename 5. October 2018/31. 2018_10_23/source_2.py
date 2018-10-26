fibo = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def word_to_sum(st):
    def letter_to_fibo(ch):
        # ord - функция, которая переводит символ в код в ASCII
        return fibo[ord(ch) - ord('A')]

    a = map(letter_to_fibo, st)
    return '+'.join(map(str, a))


if __name__ == '__main__':
    st = 'ABBBCDEFGHIJ'
    print(word_to_sum(st))
