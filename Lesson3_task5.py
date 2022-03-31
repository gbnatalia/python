from random import randrange

def get_jokes(count_joke, repeat):
    '''
    Функция формирования <count_joke> шуток из трех случайных слов, взятых из списков:
        nouns       = ["автомобиль", "лес", "огонь", "город", "дом"]
        adverbs     = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
        adjectives  = ["веселый", "яркий", "зеленый", "утопичный","мягкий"]
    :param count_joke:      число шуток, которые надо сформировать
    :param repeat:          флаг повтора использования слов из списков
    :return:                список из <count_joke> шуток
    '''
    nouns       = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs     = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives  = ["веселый", "яркий", "зеленый", "утопичный","мягкий"]

    count = count_joke
    # проверка возможности сгенерить указанное число шуток
    min_list = min(len(nouns), len(adverbs), len(adjectives))
    if count > min_list and not repeat:
        print(f"Передано недопустимое число шуток - {count}! Будет сформировано - {min_list} шуток!")
        count = min_list

    joke_list = []
    for ind in range(count):
        noun, adverb, adjective = randrange(len(nouns)), randrange(len(adverbs)), randrange(len(adjectives))
        joke_list.append(f"{nouns[noun]} {adverbs[adverb]} {adjectives[adjective]}")
        if not repeat:
            nouns.pop(noun)
            adverbs.pop(adverb)
            adjectives.pop(adjective)

    return joke_list


if __name__ == "__main__":

    print('##############################################################')
    print('#             У р о к - 3   З а д а ч а - 5                  #')
    print('#          Ф о р  м и р о в а н и е    ш у т о к             #')
    print('##############################################################')
    answer = 'y'
    while answer == 'y':

        str_count = input("Введите число шуток, которые вы хотите получить: ")
        while not str_count.isdigit():
            print(f"Введено некорректное число шуток: {str_count}")
            str_count = input("Введите число шуток, которые вы хотите получить: ")
        count = int(str_count)

        str_repeat = input('Введите возможность повтора слова в разных шутках ("y" - если "Да" / "n" - "Нет"): ')
        while str_repeat != "y" and str_repeat != "n":
            print(f"Введен некорректный ответ: {str_repeat}")
            str_repeat = input('Введите возможность повтора слова в разных шутках ("y" - если "Да" / "n" - "Нет"): ')
        if str_repeat == "y":
            rep = True
        else:
            rep = False

        goke_lst = get_jokes(repeat=rep, count_joke=count)
        print(*goke_lst, sep="\n")

        while True:
            answer = input('Вы хотите продолжить тестрирование задачи 5 ("y" - если "Да" / "n" - "Нет")?: ')
            if answer in ("y", "n"):
                break
            else:
                print(f'Введен некорректный ответ: {answer}')
