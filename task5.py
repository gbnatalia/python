'''
5. Реализовать класс Stationery (канцелярская принадлежность):
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
'''

class Stationery:
    '''    Класс канцелярской принадлежности    '''
    def __init__(self):
        self.title = "group Stationery"

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    '''    Класс ручки    '''
    def __init__(self):
        Stationery.__init__(self)

    def draw(self):
        print("I am Pen")

class Pencil(Stationery):
    '''    Класс карандаша    '''
    def __init__(self):
        Stationery.__init__(self)

    def draw(self):
        print("I am Pensil")

class Handle(Stationery):
    '''    Маркер    '''
    def __init__(self):
        Stationery.__init__(self)

    def draw(self):
        print("I am Handle")

if __name__ == "__main__":

    parent = Stationery()
    print(parent.title)
    parent.draw()

    child_pen = Pen()
    print(child_pen.title)
    child_pen.draw()

    child_pencil = Pencil()
    print(child_pencil.title)
    child_pencil.draw()

    child_handle = Handle()
    print(child_handle.title)
    child_handle.draw()