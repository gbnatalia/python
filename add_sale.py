import re
from sys import argv

if len(argv) != 2 or not bool(re.fullmatch(r'\d{4},\d{1}', argv[1])):
    print('Задано некорректное число параметров или некорректный параметр')
    print('В команду должен быть передан один аргумент - вещественное число в формате XXXX,X')
    print('Например: 1234,5')
    exit()

with open("bakery.csv", "a", encoding="utf8") as f:
    f.write(argv[1])

