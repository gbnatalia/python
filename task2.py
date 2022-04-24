'''
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определённое название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.

Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке
знания. Реализовать абстрактные классы для основных классов проекта и проверить работу
декоратора @property.
'''
from abc import ABC, abstractmethod


class clothes(ABC):
    '''    класс "Одежда"    '''
    def __init__(self):
        pass
    
    @property
    @abstractmethod
    def fabric_consumption(self):
        pass

    @property
    @abstractmethod
    def val(self):
        pass

class coat(clothes):
    '''    класс "Пальто"    '''

    def __init__(self):
        super().__init__()
        self.__V = 0

    # текущий размер
    @property
    def val(self):
        return self.__V

    # установка размера
    @val.setter
    def val(self, x):
        self.__V = x

    #подсчёт расхода ткани
    @property
    def fabric_consumption(self):
        return (self.__V /6.5 + 0.5)


class suit(clothes):
    '''    класс "Костюм"    '''

    def __init__(self):
        super().__init__()
        self.__H = 0

    # текущий рост
    @property
    def val(self):
        return self.__H

    # установка роста
    @val.setter
    def val(self, H):
        self.__H = H

    #подсчёт расхода ткани
    @property
    def fabric_consumption(self):
        return (2 * self.__H + 0.3)

if __name__ == "__main__":
    cl = coat()
    cl.val = 10
    print(cl.fabric_consumption)

    cl = suit()
    cl.val = 60
    print(cl.fabric_consumption)