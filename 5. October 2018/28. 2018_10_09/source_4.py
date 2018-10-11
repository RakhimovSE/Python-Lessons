class Triangle:
    def __init__(self, a, b, c):
        if not self.correct(a, b, c):
            print('Значения сторон введены неверно!')
            a, b, c = 3, 4, 5
        self.a = a
        self.b = b
        self.c = c

    def correct(self, a, b, c):
        if a >= b + c or b >= a + c or c >= a + b:
            return False
        return True

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    def __str__(self):
        return 'a=%.2f, b=%.2f, c=%.2f, P(a, b, c)=%.2f' % (self.a, self.b, self.c, self.perimeter)


class IsoscelesTriangle(Triangle):
    def __init__(self, a, c):
        super().__init__(a, a, c)


class RightTriangle(IsoscelesTriangle):
    def __init__(self, a):
        super().__init__(a, a)


if __name__ == '__main__':
    t1 = Triangle(8, 9, 10)
    print(t1)
    t2 = IsoscelesTriangle(5, 6)
    print(t2)
    t3 = RightTriangle(8)
    print(t3)
