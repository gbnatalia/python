'''
3. Реализовать базовый класс Worker (работник):
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров
'''


class Worker:
    '''    Класс "работник"  '''

    _income = {'wage': 100, 'bonus': 50}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = income[0]
        self._income['bonus'] = income[1]


class Position(Worker):
    ''' Класс "Позиция (должность)" '''
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return super()._income['wage'] + super()._income['bonus']

if __name__ == "__main__":
    pos = Position("Иван", "Сидоров", "программист", income=(150, 40))
    print(f"Атрибуты класса -  Имя: {pos.name}, Фамилия: {pos.surname}, Должность: {pos.position}, Доход: {pos._income['wage'] } + {pos._income['bonus']}")
    print("Полное имя: ", pos.get_full_name())
    print("Доход: ", pos.get_total_income())


