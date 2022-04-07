src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# список уникальных элементов
unicum_src = list(set(src))

# формируем список повторов
repeat_lst = src.copy()
for el in unicum_src:
    repeat_lst.remove(el)
repeat_lst = list(set(repeat_lst))

# формируем список из элементов src без повторов в порядке их следования в исх.списке
dst = [el for el in src if el not in repeat_lst]

print(dst)


