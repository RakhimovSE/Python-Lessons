# Свойства в классах

import math

class Circle:
    def __init__(self, radius):
        # По принципу инкапсуляции мы должны скрывать поля и обращаться к ним через свойства
        self.radius = radius

    # Свойство для считывания радиуса
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        """
        Вызывается, когда мы задаем значение радиуса (self.radius = 5)
        :param value:
        :return:
        """
        if type(value) != float or value < 0:
            print('Значение радиуса введено неверно! Заменено на 1')
            value = 1.0
        self.__radius = value

    @property
    def diametr(self):
        return self.radius * 2

    @property
    def length(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return 'Диаметр: {}, длина окружности: {}, площадь круга: {}'.format(self.diametr, self.length, self.area)


if __name__ == '__main__':
    c = Circle(float(input()))
    print(c)
    c.radius = 5.0
    print(c)