'''
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
 "">>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
"">>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
...
raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
'''
import re

email = re.compile(r'(?P<name>[A-Za-z0-9_]+)@(?P<host>[A-Za-z0-9_]+\.[A-Z|a-z]{2,})')

def email_parse(email_address):
    if not re.fullmatch(email, email_address):
        raise ValueError(f'wrong email:{email_address}')
    else:
        r = email.search(email_address)
        return (r.group("name"), r.group("host"))
        #return tuple(email_address.split("@"))

if __name__ == "__main__":
    lst_email = ["someone@geekbrains.ru", "someone@geekbrainsru"]
    for elem in lst_email:
        try:
            print(email_parse(elem))
        except ValueError as e:
            print(f'ValueError:{e}')
