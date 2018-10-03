class Man:
    def __init__(self, name, age, male, city):
        self.name = name
        self.age = age
        self.male = male
        self.city = city

    def info(self):
        print('Имя: {}, возраст: {}, пол: {}, город: {}'.
              format(self.name, self.age, 'мужский' if self.male else 'женский',
                     self.city))

man = Man('Василий', 22, True, 'Moscow')
man.info()
