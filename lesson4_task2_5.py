from utils import currency_rates
from sys import argv

if len(argv) > 1:
    result = currency_rates(argv[1])
else:
    print('Не задан тип валюты. Будет осуществлен запрос для значения по умолчанию ("USD")')
    result = currency_rates()

if result:
    print(f'{result[0]} {result[1]}')
else:
    print(result)
