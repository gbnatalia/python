import tkinter.filedialog as fd
import os
import json

def dict_sort(dictionary):
    '''
    Функция сортировки словаря по ключам
    :param dictionary: словарь для сортировки
    :return: отсортированный словарь по ключам
    '''
    # получили список кортежей, отсортированных по ключу
    sort_tuple = sorted(dictionary.items(), key=lambda x: x[0], reverse=True)

    # преобразуем обратно в словарь
    return dict(sort_tuple)


if __name__ == "__main__":
    file_dict = dict()

    # задание папки
    folder_name = fd.askdirectory(initialdir=os.getcwd())

    # получение списка файлов
    files = os.listdir(folder_name)

    # создание словаря по файлам
    for file in files:
        full_file_name = os.path.join(folder_name, file)
        size_file = os.stat(full_file_name)[6]
        high = 10 ** len(str(size_file))
        fn, ext = os.path.splitext(file)

        if high in file_dict.keys():
            (sch, exts) = file_dict[high]
            sch += 1
            if ext not in exts:
                exts.append(ext)
            file_dict[high] = (sch, exts)
        else:
            file_dict[high] = (1, [ext])

    # сортировка словаря по ключам
    file_dict = dict_sort(file_dict)

    print(file_dict, sep="\n")

    # сохранение данных в json файл
    with open(f'{folder_name}_summary.json', 'w') as outfile:
        json.dump(file_dict, outfile, indent=4)
