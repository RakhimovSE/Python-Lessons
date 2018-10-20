class Vehicle:
    name = 'Транспорт'

    def __init__(self, color, model):
        self.color = color
        self.model = model

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    def __str__(self):
        return 'Транспортное средство: %s, цвет: %s, модель: %s' % (Vehicle.name, self.color, self.model)


class GroundVehicle(Vehicle):
    name = 'Наземный транспорт'

    def __init__(self, color, model, power, wheel_num):
        super().__init__(color, model)
        self.power = power
        self.wheel_num = wheel_num

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        self.__power = value

    @property
    def wheel_num(self):
        return self.__wheel_num

    @wheel_num.setter
    def wheel_num(self, value):
        self.__wheel_num = value

    def __str__(self):
        result = super().__str__() + ', мощность: %d, число колес: %d' % (self.power, self.wheel_num)
        return result


class Automobile(GroundVehicle):
    name = 'Автомобиль'

    def __init__(self, color, model, power):
        super().__init__(color, model, power, 4)


class Bus(GroundVehicle):
    name = 'Автобус'

    def __init__(self, color, model, power, wheel_num):
        super().__init__(color, model, power, wheel_num)


class Tractor(GroundVehicle):
    name = 'Трактор'

    def __init__(self, color, model, power, wheel_num):
        super().__init__(color, model, power, wheel_num)


if __name__ == '__main__':
    obj1 = Automobile('red', 'Porsche', 350)
    obj2 = Bus('green', 'Mitsubishi', 400, 6)
    obj3 = Tractor('yellow', 'Ferrari', 200, 3)
    print(obj1)
    print(obj2)
    print(obj3)
