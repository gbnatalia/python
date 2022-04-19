'''
2. *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6
урока nginx_logs.txt (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
для получения информации вида:
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
например:
    raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
    parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
'''

import re

regix = re.compile('^(?P<remote_addr>(((^|:)([0-9a-fA-F]{0,4})){1,8})|'
                   '((2[0-5]|1[0-9]|[0-9])?[0-9]\.){3}((2[0-5]|1[0-9]|[0-9])?[0-9]))'
                   '\ -\ -\ \[(?P<request_datetime>.+)\]\ \"(?P<request_type>\w+)\ '
                   '(?P<requested_resource>.+)\"\ (?P<response_code>\d+)\ (?P<response_size>\d+)\ \".+\"\ \".+\"')

def get_parsed_raw(raw):
    res = regix.search(raw)
    if res is None:
        return None
    #return res.groups()
    return (res.group('remote_addr'), res.group('request_datetime'), res.group('request_type'),
            res.group('requested_resource'), res.group('response_code'), res.group('response_size'))

if __name__ == "__main__":
    with open("nginx_logs.txt", "r", encoding="utf8") as f:
        for raw in f:
            parser_raw = get_parsed_raw(raw)
            if not parser_raw is None:
                print(parser_raw)
