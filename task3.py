import os
import shutil

def copytree(src, dst):
    '''
    Функция копирования дерева с заменой совпадающих файлов.
    Прочие файлы не трогает
    :param src:  исходная директория, файлы которой (папки и файлы) надо скопировать
    :param dst:  директория назначения
    '''
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            if not os.path.exists(d):
                os.mkdir(d)
            copytree(s, d)
        else:
            if os.path.exists(d):
                os.remove(d)
            shutil.copy(s, d)

def move_dir(dst_path, src_path, find_dir_name):
    '''
    функция перемещения содержимого директории с именем find_dir_name c уничтожением исх.директории
    в директорию dst_path
    :param dst_path:        путь куда надо перенести содержимое директории с именем find_dir_name
    :param src_path:        исходный путь откуда осуществляется поиск директории с именем find_dir_name
    :param find_dir_name:   имя перемещаемой директории
    '''
    for elem in os.listdir(src_path):
        new_path = os.path.join(src_path, elem)
        if os.path.isdir(new_path):
            if elem == find_dir_name:
                copytree(new_path, dst_path)
                shutil.rmtree(new_path)
            else:
                move_dir(dst_path, new_path, find_dir_name)

if __name__ == "__main__":

    # корневой элемент
    root = os.path.join(os.getcwd(), "my_project")

    # создаем директорию templates чтобы условия для всех вхождений "templates" были одинаковые
    res_dirs = os.path.join(root, "templates")
    if not os.path.exists(res_dirs):
        os.mkdir(res_dirs)

    # отдельно выносим цикл по верхним директориям, чтобы создаваемая директория не входила в обход
    for dir in os.listdir(root):
        new_root = os.path.join(root, dir)
        try:
            # вызов функции рекурсивного поиска вхождений директории templates и ее перемещения
            move_dir(res_dirs, new_root, "templates")
        except Exception as e:
            print(f'Ошибка перемещения директорий "templates": {e}')