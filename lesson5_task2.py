try:

    n = int(input('Введите n - максимальное значение для генерации списка нечетных чисел: '))
    gen_obj = (x for x in range(1, n+1, 2))
    print(type(gen_obj))
    for el in gen_obj:
        print(el)

except ValueError:
    print("Вы ввели некорректное число. Запустите программу заново")
