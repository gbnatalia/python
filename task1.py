'''
Реализовать класс "Дата", функция конструктор которого должна принимать дату в виде строки
формата "день-месяц-год". В рамках класса реализовать два метода. Первый - с декоратором
@classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу "Число".
Второй - с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц от 1-12). Проверить работу полученной структуры на реальных данных.
'''

class My_Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split('-'):
            my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 > day or day > 31:
            return f'Некорректное значение дня - {day}'
        if month < 1 or month > 12:
            return f'Некорректное значение месяца - {month}'
        if year > 2023 or year < 0:
            return f'Некорректное значение года - {year}'
        return "Все Ок!"

    def __str__(self):
        day, month, year = My_Data.extract(self.day_month_year)
        return f'Текущая дата: {day}.{month}.{year}'


if __name__ == "__main__":

    dt = My_Data('22-01-1971')
    print(dt)
    day, month, year = My_Data.extract('22-01-1971')
    print(My_Data.valid(day, month, year))
    print(My_Data.valid(*My_Data.extract('22-01-1971')))
    print(My_Data.valid(*dt.extract('22-01-1971')))

    print(My_Data.valid(*My_Data.extract('0-01-1971')))
    print(My_Data.valid(*My_Data.extract('40-01-1971')))
    print(My_Data.valid(*My_Data.extract('22-0-1971')))
    print(My_Data.valid(*My_Data.extract('22-13-1971')))
    print(My_Data.valid(*My_Data.extract('22-01-4000')))
