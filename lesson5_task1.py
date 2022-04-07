def get_odd(n):
    for x in range(1, n+1, 2):
        yield x

if __name__ == "__main__":
    res = 0
    try:
        n = int(input('Введите n - максимальное значение для генерации нечетных чисел: '))
        gen_obj = get_odd(n)
        print(type(gen_obj))
        for el in gen_obj:
            print(el)
    except ValueError:
        print("Вы ввели некорректное число. Запустите программу заново")



