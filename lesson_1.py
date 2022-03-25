def lesson1_task1():
    '''
    Функция реализации вывода информации о промежутке времени в зависимости
    от его продолжительности duration в секундах:
    a: до минуты <s> сек;
    b: до часа <m> мин <s> сек;
    c: до суток <h> час <m> мин <s> сек
    d: в остальных случаях: <d> дн <h> час <m> мин <s> сек
    '''

    game = "yes"

    print("##########################################")
    print("#    Программа преобразования времени    #")
    print("##########################################")

    while game == "yes":

        try:
            # приглашение пользователю
            src_sec = int(input("Введите число секунд: "))
        except ValueError:
            print("Введено некорректное значение числа секунд! Попробуйте еще!")
            continue

        # проверка корректности введенного времени
        if src_sec < 0:
            print("Введено некорректное значение числа секунд! Попробуйте еще!")
            continue

        # конвертация времени в дни, часы, минуты, секунды
        days = src_sec // 86400      # 86400 = 3600 * 24
        remains = src_sec % 86400
        hours = remains // 3600
        remains = remains % 3600
        minutes = remains // 60
        seconds = remains % 60

        # вывод преобразованного времени на экран
        if days:
            print(f"Результат: {days} дн {hours} час {minutes} мин {seconds} сек")
        elif hours:
            print(f"Результат: {hours} час {minutes} мин {seconds} сек")
        elif minutes:
            print(f"Результат: {minutes} мин {seconds} сек")
        else:
            print(f"Результат: {seconds} сек")

        # можно через time, datatime:
        # import time, time.gmtime(src_sec), time.strftime("%H час %M мин %S сек", convert_time)

        # запрос пользователя о желании продолжить преобразование времени
        game = input("Вы хотите далее заниматься преобразованием времени? (yes/no): ")
        while game != "yes" and game != "no":
            print(f'Ответ {game} не понятен! Введите "yes" или "no"')
            game = input("Вы хотите далее заниматься преобразованием времени? (yes/no): ")

    print("\nРабота программы завершена. Всего доброго!")

def get_sum(number):
    summa = 0
    list_nums = [int(el) for el in str(number)]
    for num in list_nums:
        summa += num
    return summa

def lesson1_task2():
    '''
    Функция формирования списка, состоящего из кубов нечётных чисел от 1 до 1000.
    С этим списком осуществляется:
    a. Вычисление суммы тех чисел из списка, сумма цифр которых делится нацело на 7.
    b. К каждому элементу списка добавляется 17 и заново вычисляется сумма
       тех чисел из этого списка, сумма цифр которых делится нацело на 7.
    Результаты вычислений и преобразований выводятся на печать
    '''
    lst = [x**3 for x in range(1, 1001, 2)]
    print("")
    print(f"Исходный список:")
    for i in range(len(lst)):
        if (i+1) % 8 == 0 or i == len(lst)-1:
            print(f"{lst[i]:>10}")
        else:
            print(f"{lst[i]:>10}", end=", ")

    summa = 0
    summa_17 = 0

    for i in range(len(lst)):

        # Запрет использования неарифметических операций?
        #if sum([int(el) for el in str(lst[i])]) % 7:
        if get_sum(lst[i]) % 7 == 0:
            summa += lst[i]

        # Формирование элемента преобразованного списка
        lst[i] += 17

         # Запрет использования неарифметических операций?
        #if sum([int(el) for el in str(lst[i])]) % 7:
        if get_sum(lst[i]) % 7 == 0:
            summa_17 += lst[i]

    print(f"Сумма чисел сумма цифр которых делится на 7 без остатка в исходном списке: {summa}")
    print("")
    print(f"Преобразованный список:")
    for i in range(len(lst)):
        if (i+1) % 8 == 0 or i == len(lst)-1:
            print(f"{lst[i]:>10}")
        else:
            print(f"{lst[i]:>10}", end=", ")
    print(f"Сумма чисел сумма цифр которых делится на 7 без остатка в преобразованном списке: {summa_17}")

def lesson1_task3():
    '''
    Функция склонения слова процент в фразе "N процентов".
    Выводит полученые фразы отдельными строками для чисел в диапазоне от 1 до 100.
    '''
    for number in range(1, 101):
        if number < 2:
            print(f"{number} процент")
        elif number < 5:
            print(f"{number} процента")
        elif number > 20:
            remains = number % 10
            if remains == 1:
                print(f"{number} процент")
            elif remains and remains < 5:
                print(f"{number} процента")
            else:
                print(f"{number} процентов")
        else:
            print(f"{number} процентов")



if __name__ == "__main__":
    try:
        num_task = int(input('Введите номер задачи для тестирования из диапазона 1-3: '))
    except ValueError:
        print("Вы ввели некорректное число. Запустите программу заново")
        quit()

    lst_tasl = [lesson1_task1, lesson1_task2, lesson1_task3]
    if num_task > -1 and num_task < 4:
        lst_tasl[num_task - 1]()
    else:
        print("Вы ввели некорректное число. Запустите программу заново")
