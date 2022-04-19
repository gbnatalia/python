'''
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
...
@val_checker(lambda x: x > 0)
def calc_cube(x):
return x ** 3
#>>> a = calc_cube(5)
125
#>>> a = calc_cube(-5)
Traceback (most recent call last):
raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
'''

def val_checker(callback_func):
    def decorator(func):
        def wrapper(x):
            if not callback_func(x):
                raise ValueError(f"ValueError: wrong val {x}")
            return func(x)
        return wrapper
    return decorator

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

if __name__ == "__main__":
    # вызов функции без декоратора
    orig_calc_cube = calc_cube.__closure__[1].cell_contents
    print(orig_calc_cube)   #подтверждение что именно наша функция
    a = orig_calc_cube(7)
    print(a)

    print()

    # использование callback функции
    try:
        a = calc_cube(5)
        print(a)

        a = calc_cube(-5)
        print(a)

    except ValueError as e:
        print(e)
