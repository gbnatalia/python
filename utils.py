from requests import get, utils
from datetime import datetime
import xml.etree.ElementTree as ET
from decimal import Decimal
from sys import argv

def currency_rates(CharCode = "USD"):
    '''
    Функция получения курса валюты по отношению к рублю
    :param CharCode: код код валюты (например, USD, EUR, GBP, ...)
    :return: список, содержащий курс валюты по отношению к рублю типа Decimal и
                     дату, передаваемую в ответе сервера типа Date
    '''
    url = "http://www.cbr.ru/scripts/XML_daily.asp?"
    response = get(url)
    result = None
    if response.status_code == 200:
        encodings = utils.get_encoding_from_headers(response.headers)
        content = response.content.decode(encoding=encodings)
        rootnode = ET.fromstring(content)
        for i in range(len(rootnode)):
            if rootnode[i][1].text == CharCode.upper():
                dt = datetime.strptime(rootnode.get('Date'), "%d.%m.%Y").date()
                result = [Decimal(rootnode[i][4].text.replace(",", ".")), dt]
                break
    else:
        print('Ошибка выполнения запроса к серверу')
    return result

if __name__ == "__main__":
    if len(argv) > 1:
        result = currency_rates(argv[1])
    else:
        print('Не задан тип валюты. Будет осуществлен запрос для значения по умолчанию ("USD")')
        result = currency_rates()

    if result:
        print(f'{result[0]} {result[1]}')
    else:
        print(result)

