'''
    4. Создать класс, описывающий склад оргтехники.
    А также класс "Оргтехника", который будет базовым для классов-наследников
    Эти классы - конкретные типы оргтехники (принтер, сканер, ксерокс).
    В базовом классе определить параметры общие для приведенных типов.
    В классах-наследниках реализовать параметры, уникальные для  каждого типа оргтехники
    5. Разработать методы, отвечающие за прием оргтехники на склад и передачу
    в определенное подразделение компании.
    Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных
    можно использовать любую подходящую структуру (например словарь).
    6. Реализовать механизм валидации вводимых пользователем данных.
    Например, для указания колличества единиц, отправляемых на склад нельзя использовать
    строковый тип данных
'''
import re

regix = re.compile('^[0-9]*')

class Office_equipment_warehouse:
    ''' Класс "Склад оргтехники" '''

    # конструктор класса
    def __init__(self):
        self.__inv = {}

    def my_decorator(func):
        def wrapper(self, equipment, count):
            if regix.fullmatch(count) == None:
                print(f"Передано количество товаров = {count}. Количество товаров должно быть целым числом!!!")
                return None
            return func(self, equipment, count)

        return wrapper

    # добавление {count} единиц товара
    @my_decorator
    def add_equipment(self, equipment, count):
        print(f"\nДобавление на склад {count} товаров типа '{equipment.type}' модели '{equipment.model}'")
        add_cnt = int(count)
        if equipment.type in self.__inv.keys():
            for model, cnt in self.__inv[equipment.type]:
                if equipment.model == model:
                    cnt += add_cnt
                    self.__inv[equipment.type][model] = cnt
                    break
            else:
                self.__inv[equipment.type].append([equipment.model, add_cnt])
        else:
            self.__inv[equipment.type] = []
            self.__inv[equipment.type].append([equipment.model, add_cnt])

    # извлечение {count} единиц товара для передачи в отдел
    @my_decorator
    def extract_equipment(self, equipment, count):
        print(f"\nЗапрос выдачи со склада {count} товаров типа '{equipment.type}' модели '{equipment.model}'")
        del_cnt = int(count)

        if equipment.type in self.__inv:
            lst = self.__inv[equipment.type]
            for index in range(len(lst)):
                if equipment.model == lst[index][0]:
                    if lst[index][1] < del_cnt:
                        print(f"Запрошено товара больше, чем есть в наличие. Будет выдано {lst[index][1]} единиц товара")
                        lst.pop(index)
                        if not len(lst):
                            del self.__inv[equipment.type]
                    else:
                        print("Товар выдан")
                        if lst[index][1] > del_cnt:
                            lst[index][1] -= del_cnt
                        else:
                            lst.pop(index)
                            if not len(lst):
                                del self.__inv[equipment.type]
                    break
            else:
                print(f"Модели '{equipment.model}' товара '{equipment.type}' нет на складе")
        else:
            print(f"Товара '{equipment.type}' нет на складе")


    # перечень имеющейся оргтехники
    def Inventory(self):
        print("\nПеречень оргтехники, имеющейся на складе:")

        for type_equipment in self.__inv:
            print(f'{type_equipment}:')

            for model, count in self.__inv[type_equipment]:
                print(f"\tмодель: '{model}' - {count} штук")

class Office_equipment:

    ''' Класс "Оргтехника" '''
    def __init__(self, type_equipment, model):
        self.__type = type_equipment
        self.__model = model

    @property
    def model(self):
        return self.__model

    @property
    def type(self):
        return self.__type

    def __str__(self):
        return f"{self.__type}: модель - '{self.__model}'"


class Printer(Office_equipment):
    ''' Класс "Принтер" '''
    def __init__(self,  model):
        super().__init__("Принтер", model)

    def description(self):
        return f"Принтер '{self.model}'.Предназначен для печати документов"

class Scaner(Office_equipment):
    ''' Класс "Сканер" '''
    def __init__(self, model):
        super().__init__("Сканер", model)

    def description(self):
        return "Предназначен для сканирования документов"

class Xerox(Office_equipment):
    ''' Класс "Ксерокс" '''

    def __init__(self, model):
        super().__init__("Ксерокс", model)

    def description(self):
        return "Предназначен для создание ксерокса документов"


if __name__ == "__main__":
    # создание объекта склада оргтехники
    warehouse = Office_equipment_warehouse()

    # создание объектов принтеров
    pr1 = Printer("hp")
    print(pr1)
    print(pr1.description())
    warehouse.add_equipment(pr1, '100')
    warehouse.Inventory()
    print("---------------------------------")

    pr2 = Printer("canon")
    print(pr2)
    print(pr2.description())
    warehouse.add_equipment(pr2, '80')
    warehouse.Inventory()
    print("---------------------------------")

    # создание объектов сканеров
    sc1 = Scaner("Fujitsu")
    print(sc1)
    print(sc1.description())
    warehouse.add_equipment(sc1, '30')
    warehouse.Inventory()
    print("---------------------------------")

    sc2 = Scaner("Epson")
    print(sc2)
    print(sc2.description())
    warehouse.add_equipment(sc2, '20')
    warehouse.Inventory()
    print("---------------------------------")

    # создание объека ксерокса
    xerox1 = Xerox("Ricoh")
    print(xerox1)
    print(xerox1.description())
    #warehouse.add_equipment(xerox1, '20')
    #warehouse.Inventory()
    print("---------------------------------")

    #выдача товаров
    warehouse.extract_equipment(sc2, '10')
    warehouse.Inventory()

    pr3 = Printer("Epson")
    warehouse.extract_equipment(pr3, '10')
    warehouse.Inventory()

    warehouse.extract_equipment(xerox1, '10')
    warehouse.Inventory()

    warehouse.extract_equipment(sc2, '10')
    warehouse.Inventory()

    warehouse.extract_equipment(sc2, '10aaaaa')
    warehouse.Inventory()
