'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
    31 22
    37 43
    51 86

    3 5 32
    2 4 6
    -1 64 -8

    3 5 8 3
    8 3 7 1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
'''
from copy import deepcopy

class Matrix:
    '''
    Класс "Матрица"
    '''

    def __init__(self, list_of_lists):
        self.matrix = deepcopy(list_of_lists)

    def __str__(self):
        res_str = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                res_str = f'{res_str} {self.matrix[i][j]}'
            if i != len(self.matrix)-1:
                res_str = f'{res_str}\n'
        return res_str

    def __add__(self, other):
        sum_matrix = []
        try:
            for i in range(len(self.matrix)):
                row_matrix = []
                for j in range(len(self.matrix[0])):
                    summa = self.matrix[i][j] + other.matrix[i][j]
                    row_matrix.append(summa)
                sum_matrix.append(row_matrix)
        except:
            print('Ошибка сложения матриц. Проверьте совпадение размерностей матриц, а также типы данных в матрицах')
            return None
        return Matrix(sum_matrix)

if __name__ == "__main__":
    list_of_lists1 = [[31, 22],[37, 43], [51, 86]]
    m1 = Matrix(list_of_lists1)
    print(f'матрица1: \n{m1}\n')

    list_of_lists2 = [[12, 34],[56, 78], [90, 12]]
    m2 = Matrix(list_of_lists2)
    print(f'матрица2: \n{m2}\n')

    print(f'Результирующая матрица: \n{m1+m2}\n')

    list_of_lists3 =[[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
    m3 = Matrix(list_of_lists3)
    print(f'матрица3: \n{m3}\n')

    list_of_lists4 =[[3, 5, 8, 3], [8, 3, 7, 1]]
    m4 = Matrix(list_of_lists4)
    print(f'матрица4: \n{m4}\n')


