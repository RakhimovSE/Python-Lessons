class Man:
    def __init__(self, name, age, male, city):
        self.name = name
        self.age = age
        self.male = male
        self.city = city

    def __str__(self):
        return 'Имя: {}, возраст: {}, пол: {}, город: {}'.format(self.name, self.age, 'мужский' if self.male else 'женский',self.city)

def add():
    global men
    name = input("Имя:")
    age = int(input("Возраст:"))
    male = True if input("Пол:") =="м" else False
    city = input("Город:")
    man = Man(name,age,male,city)
    men.append(man)

def show():
    global men
    for man in men:
        print(man)

def def_cmd():
    print('Команда не найдена')

men = []
commands = {
    "add": add,
    "show": show
    }

command = input("Enter command: ")
while command != "exit":
    cmd = commands.get(command, def_cmd)
    cmd()
    command = input("Что хотите? ")
