from sys import argv

def create_dict(file_users = "users.csv", file_hobby = "hobby.csv", file_result = "users_hobby.txt"):

    try:
        u_file = open(file_users, "r", encoding="utf8")
    except: # FileNotFoundError:
        return 2

    try:
        h_file = open(file_hobby, "r", encoding="utf8")
    except: # FileNotFoundError:
        return 3

    with open(file_result, "w", encoding="utf8") as r_file:
        while (True):
            # чтение текущих строк из файлов
            try:
                u = u_file.readline()
            except IOError:
                return 4
            try:
                h = h_file.readline()
            except IOError:
                return 5

            # проверка окончания какого-либо файла
            if u == "":
                if h != "":
                    return 1
                else:
                    break
            elif h == "":
                h = "None"

            # убираем символы конца строки
            if u.find('\n') != -1:
                u = u[:-1]
            if h.find('\n') != -1:
                h = h[:-1]

            # склейка в результирующую строку
            str = f"{' '.join(u.split(','))}: {h}\n"

            # запись в файл
            r_file.write(str)

    return 0

if __name__ == "__main__":
    res = 0
    if len(argv) == 4:
        res = create_dict(argv[1], argv[2], argv[3])
    elif len(argv) == 1:
        res = create_dict()
    else:
        print("Введена некорректная команда!")

    if res == 1:
        print("Перечень хобби превышает число пользователей!")
    elif res == 2:
        print("Ошибка открытия файла имен пользователей!")
    elif res == 3:
        print("Ошибка открытия файла c хобби!")
    elif res == 4:
        print("Ошибка чтения файла имен пользователей!")
    elif res == 5:
        print("Ошибка чтения файла с хобби!")