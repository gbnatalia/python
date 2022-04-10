from sys import argv
from os.path import getsize, exists

# проверка корректности переданных аргументов командной строки
for el in argv[1:]:
    #if not isinstance(el, int):
    if not el.isdigit():
        print(f'Передан некорректный аргумент -"{el}"')
        exit()
    elif int(el) < 1:
        print(f'Передан некорректное значение параметра -"{el}".Значение не может быть < 1')
        exit()

if len(argv) > 3:
    print(f'Передано некорректное число параметров - "{len(argv)-1}"')
    exit()

if len(argv) == 3 and int(argv[2]) < int(argv[1]):
    print(f'Начальный индекс чтения ("{argv[1]}") <  конечного ("{argv[2]}")')
    exit()

# определение индексов начала и конца чтения
num_start = 0
num_end = getsize("bakery.csv") // 6

if len(argv) > 1:               # если задано начало чтения
    if int(argv[1]) > num_end:
        num_start = num_end
    elif int(argv[1]) > 0:
        num_start = int(argv[1])

    if len(argv) > 2:               # если задано конец чтения
        if int(argv[2]) < num_end:
            num_end = int(argv[2]) + 1

with open("bakery.csv", encoding="utf8") as f:
    f.seek(num_start * 6)
    for i in range(num_end - num_start):
        print(f.read(6))
