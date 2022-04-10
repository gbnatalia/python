def parser(line):
    '''
    парсер строки вида:
    80.91.33.133 - - [17/May/2015:08:05:07 +0000] "GET /downloads/product_1 HTTP/1.1"
     304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"
    Формирует и выводит на печать кортеж  вида:
    ('80.91.33.133', 'GET', '/downloads/product_1 HTTP/1.1')
    :param line: исходная строка
    :return:     ip-адрес запроса
    '''
    m = line.split()
    line_tuple = (m[0], m[5][1:], m[6])
    print(line_tuple)
    return m[0]

if __name__ == "__main__":
    max_sch = 0
    spammer  = "нет"
    with open("nginx_logs.txt", "r", encoding="utf8") as f:
        ip_dict = dict()
        for line in f:
            ip_adr = parser(line)

            if ip_adr in ip_dict.keys():
                sch = ip_dict[ip_adr] + 1
                if sch > max_sch:
                    max_sch = sch
                    spammer = ip_adr
            else:
                sch = 1
            ip_dict[ip_adr] = sch

            # для того чтобы словарь не перегружал память можно хранить
            # в нем определенное количество элементов, очищая по каким то параметрам
            # например производить очищение и подведение итогов за какой-то период времени
            # есть вероятность потери какого то числа обращений спамера,
            # но и вероятность его отлова большая
            # в данной реализации используется отсев 30 записей с наименьшим числом обращений
            # при достижении общего числа записей в словаре значения 50
            if len(ip_dict) > 50:
                sort_val = sorted(ip_dict.values())
                for i in sort_val[:30]:
                    for key in ip_dict.keys():
                        if ip_dict[key] == i:
                            ip_dict.pop(key)
                            break

    min_appeal = 10 # минимальное число обращений, которые принимаются в расчет
    if max_sch > min_appeal:
        print(f'\nНаибольшее число обращений ({max_sch}) у "{spammer}"')
        sort_val = sorted(ip_dict.values(), reverse=True)
        if sort_val[1] > min_appeal:
            print("\nПодозрительные адреса:")
            print("============================================================")
            print("                   Адрес:                 | Число обращений:")
            print("============================================================")
            for i in sort_val[:10]:
                if i < min_appeal:
                    break
                for key in ip_dict.keys():
                    if ip_dict[key] == i:
                        print(f'{key} {" "*(40-len(key))} |  {i}')
                        break
    else:
        print("Спамер не обнаружен")


