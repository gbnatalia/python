def num_translate_adv(en_num):
    '''
    Функция перевода наименований чисел от 0 до 10 с английского на русский.
    Если исходное наименование числа начинается с заглавной буквы, то и результат с заглавной
    иначе с строчной
    :param en_num:  наименование числа на английском языке
    :return:        наименование числа на русском языке, если входной параметр допустим,
                    иначе None
    '''
    dictionary = {
        "zero": "ноль",
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }

    if en_num.lower() in dictionary.keys():
        if en_num.istitle():
            return dictionary[en_num.lower()].title()
        else:
            return dictionary[en_num]
    else:
        return None

if __name__ == "__main__":
    print('##############################################################')
    print('#             У р о к - 3   З а д а ч а - 3                  #')
    print('#        П е р е в о д   ч и с е л   о т   0   д о   10      #')
    print('##############################################################')

    answer = "y"
    while answer == "y":
        print("Перевод: ", num_translate_adv(input("Введите наименование числа от 0 до 10 на английском языке: ")))

        while True:
            answer = input('Будете ли еще переводить числа (введите "у" - если "Да" и  "n" - если "Нет")? ')
            if answer in ("y", "n"):
                break
            else:
                print(f"Ответ {answer} не понятен!")