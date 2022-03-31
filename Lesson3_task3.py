def thesaurus_adv(*names):
    '''
    Фукнция формирования словаря следующего вида:
        {
            "А": {
                "П": ["Петр Алексеев"]
                },
            "И": {
                "И": ["Илья Иванов"]
                },
            "С": {
                "И": ["Иван Сергеев", "Инна Серова"],
                "А": ["Анна Савельева"]
                }
        }
    из переданных пар <Имя> и <Фамилия>, разделенных пробелом.
    :param names: имена сотрудников, состоящие из пар <Имя> и <Фамилия>, разделенных пробелом
    :return:      словарь, в котором ключи - первые буквы имен, а значения списки,
                  содержащие имена, начинающеся с соответствующей буквы
    '''

    name_dict = dict()
    for fullname in list(names):
        name, family = fullname.split()
        sub_dict = dict()
        lst = list()

        if family[0].upper() in name_dict.keys():
            sub_dict = name_dict[family[0].upper()]
            if name[0].upper() in sub_dict:
                lst = sub_dict[name[0].upper()]
        lst.append(fullname)
        sub_dict[name[0].upper()] = lst
        name_dict[family[0].upper()] = sub_dict
    return name_dict

def print_dictionary(name_dict):
    '''
    Форматированный вывод словаря в виде:
        {
            "А": {
                "П": ["Петр Алексеев"]
                },
            "И": {
                "И": ["Илья Иванов"]
                },
            "С": {
                "И": ["Иван Сергеев", "Инна Серова"],
                "А": ["Анна Савельева"]
                }
        }
    :param name_dict: словарь для вывода на печать
    '''
    print_sep = ","
    print_sep_no = ""
    print("Словарь:")
    print('{', end="")
    first_fam = True
    for key1, val1 in name_dict.items():
        print(f"{print_sep if not first_fam else print_sep_no}\n\t\"{key1}\": {{", end="")
        first_fam = False
        first_name = True
        for key2, val2 in val1.items():
            print(f'{print_sep if not first_name else print_sep_no}\n\t\t"{key2}": {{\n\t\t\t{val2}\n\t\t}}', end="")
            First_name = False
        print('\n\t}', end="")
    print('\n}')

if __name__ == "__main__":

    print('##############################################################')
    print('#             У р о к - 3   З а д а ч а - 3                  #')
    print('#        Ф о р м и р о в а н и е   с л о в а р я             #')
    print('##############################################################')

    str_names = input('Введите через запятую список полных имен (<Имя> <Фамилия>) для формирования словаря: \n\r')
    str_names = ' '.join(str_names.split())       # убираем все двойные пробелы
    lst_names = str_names.split(",")              # формируем список
    lst_names = list(map(str.strip, lst_names))   # убираем лишние пробелы, если пользователь ввел Имена через запятую с пробелом
    name_dict = thesaurus_adv(*lst_names)         # формируем словарь
    print_dictionary(name_dict)                   # печатаем словарь


