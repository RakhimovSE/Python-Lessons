class Base:
    def __init__(self, param1):
        self.param1 = param1

    def __str__(self):
        return 'param1: {}'.format(self.param1)


class Class1(Base):
    def __init__(self, param1, param2):
        super().__init__(param1)
        self.param2 = param2

    def __str__(self):
        result = super(Class1, self).__str__()
        return result + '\nparam2: {}'.format(self.param2)


if __name__ == '__main__':
    obj1 = Base(1)
    obj2 = Class1(2, 3)
    print('obj1:')
    print(obj1)
    print('\nobj2:')
    print(obj2)