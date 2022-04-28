'''
Создать собственный класс-исключение, обрабатывающий ситуацию деления на 0.
Проверить его работу на данных, вводимых пользователем.
При вводе 0 в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой
'''

class MyZeroDivisionError(Exception):
    ''' Класс исключения '''
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'MyZeroDivisionError: {self.message}' if self.message else "MyZeroDivisionError: Деление на ноль!!!"


class MyDevide:
    ''' Класс деления'''
    def __init__(self, ch1, ch2):
        if ch2 == 0:
            raise MyZeroDivisionError("Введено некорректное значение знаменателя! Знаменатель не должен быть равен 0!")
            self.result = None
        self.result = ch1 / ch2

    def __str__(self):
        return f"Результат деления: {self.result}"


if __name__ == "__main__":

    try:
        ch1 = int(input('Введите числитель (целое число): '))
        ch2 = int(input('Введите знаменатель (целое число): '))
        print(MyDevide(ch1, ch2))
    except MyZeroDivisionError as e:
        print(e)
    except:
        print("Введено не целое число")

