class Class:
    def __init__(self, visible, hidden):
        self.visible = visible
        self.__hidden = hidden

    @property
    def get_hidden(self):
        return self.__hidden

    def visible_method(self):
        print('This method is visible')

    def __hidden_method(self):
        print('This method is hidden')


if __name__ == '__main__':
    obj = Class(1, 2)
    print(obj.visible)
    try:
        print(obj.__hidden)
    except Exception as ex:
        print(ex)
        print(obj.get_hidden)

    obj.visible_method()
    try:
        print(obj.__hidden_method())
    except Exception as ex:
        print(ex)