from time import perf_counter
from sys import  getsizeof

def gen_tuple(tutors, klasses):
    for i in range(len(tutors)):
        if i < len(klasses):
            yield (tutors[i], klasses[i])
        else:
            yield (tutors[i], None)

if __name__ == "__main__":
    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Наталья', 'Артем']
    klasses = ['9A', '7B', '9Б', '9В', '8Б', '10А', '10Б', '9А']

    start = perf_counter()
    gen_obj = gen_tuple(tutors, klasses)
    print("Время выполнения:", perf_counter()-start)
    print("Размер памяти:", getsizeof(gen_obj))
    print("Тип объекта:", type(gen_obj))

    for el in gen_obj:
        print(el)


