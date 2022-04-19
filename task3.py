'''
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...

@type_logger
def calc_cube(x):
    return x ** 3

#>>> a = calc_cube(5)
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
функции, например, в виде:
#>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
'''


def type_logger(func):
    def wrapper(*args, **kwargs):
        lst = []
        for param in args:
            lst.append(f'{param}: {type(param)}')

        for key, values in kwargs.items():
            lst.append(f'{key}={values}: {type(values)}')

        print(*lst, sep=", ")

        return func(*args, **kwargs)

    return wrapper

@type_logger
def abstract_func(*args, **kwargs):
    pass

@type_logger
def calc_cube(x):
    return x ** 3

if __name__ == "__main__":
    print(calc_cube(2))
    abstract_func(3, "7", a=5, b=(3, 5))
