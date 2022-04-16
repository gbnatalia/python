import os

def create_file(text):
    f = open(text, "w", encoding="utf8")
    f.close()

def parser_folder(text):
    count = text.count(".")
    lst_dir = text.split(".")
    for directory in lst_dir:
        if not os.path.isdir(directory):
            os.mkdir(directory)     #создание директории
        os.chdir(directory)         #делаем ее текущей
    # комментарий: можно было сделать с помощью makedirs
    # но была бы сложность с установкой текущей директории
    # (нужно для правильного размещения файлов)

def parser_line(src_dir, line):
    text = line
    if text[0] == '[':
        text = text[1:]
        pos = text.find("]")
        if pos == -1:
            print('ошибка в конфигурационном файле')
            return
        os.chdir(src_dir)
        text = text[:pos]
        parser_folder(text)
    else:
        if text[-1] == '\n':
            text = text[:-1]
        create_file(text)

def create_file_tree(src_dir, file_name = "config.yaml"):
    try:
        with open(file_name, 'r', encoding="utf8") as f:
            for line in f:
                parser_line(src_dir, line)
    except FileNotFoundError as e:
        print(f'Ошибка работы с файлом. Файл не найден')
    except EOFError as e:
        print(f'Ошибка работы с файлом. Неожиданный конец файла')
    except Exception as e:
        print(f'Ошибка работы: {e}')

if __name__ == "__main__":
    create_file_tree(os.getcwd())
