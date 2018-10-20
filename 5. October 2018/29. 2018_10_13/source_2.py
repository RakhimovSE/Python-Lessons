class MyDict:
    def __init__(self):
        self.keys = []
        self.values = []

    def __getitem__(self, key):
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return self.values[i]
        # выбрасывание (генерация) исключения
        raise KeyError('Ключ не найден!')

    def __setitem__(self, key, value):
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.values[i] = value
                return
        self.keys.append(key)
        self.values.append(value)

    def __str__(self):
        raw_array = []
        for key, value in zip(self.keys, self.values):
            raw_array.append('{}: {}'.format(key, value))
        result = '{ ' + ', '.join(raw_array) + ' }'
        return result


if __name__ == '__main__':
    d = MyDict()
    d['key1'] = 'value1'
    d['key2'] = 2
    d['key3'] = True

    print(d['key1'])
    d['key1'] = 'new_value1'
    print(d['key1'])
    # вызов метода __str__
    print(d)
    # будет выброшено исключение, т.к. ключ не существует
    print(d['key99'])
