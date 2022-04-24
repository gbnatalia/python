'''
Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс «Клетка». В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число).

В классе должны быть реализованы методы перегрузки арифметических операторов:
    сложение (__add__()),
    вычитание (__sub__()),
    умножение (__mul__()),
    деление (__floordiv____truediv__()).

Эти методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и округление до целого числа деления клеток соответственно.

Сложение.   Объединение двух клеток. При этом число ячеек общей клетки должно равняться
            сумме ячеек исходных двух клеток.

Вычитание.  Участвуют две клетки. Операцию необходимо выполнять, только если разность
            количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение.  Создаётся общая клетка из двух. Число ячеек общей клетки — произведение
            количества ячеек этих двух клеток.

Деление.    Создаётся общая клетка из двух. Число ячеек общей клетки определяется как
            целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом
случае метод make_order() вернёт строку: *****\n*****\n**.
Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод
make_order() вернёт строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
'''

class organic_cell:
    '''
    класса "Клетка"
    '''

    # конструктор класса
    def __init__(self, cell_count):
        self.count = cell_count

    # сложение
    def __add__(self, add_cell):
        return organic_cell(self.count + add_cell.count)

    # вычитание
    def __sub__(self, sub_cell):
        return organic_cell(self.count - sub_cell.count)

    # умножение
    def __mul__(self, mul_cell):
        return organic_cell(self.count * mul_cell.count)

    # деление нацело
    def __floordiv__(self, del_cell):
        if del_cell.count == 0:
            return None
        return organic_cell(self.count // del_cell.count)

    # деление
    #def __truediv__(self, del_cell):
    #    if del_cell.count == 0:
    #        return None
    #    return organic_cell(self.count / del_cell.count)

    # организация ячеек клетки по рядам
    def make_order(self, count_cells_in_row):
        if self.count % count_cells_in_row:
            return '*****\n' * (self.count//count_cells_in_row) + '*' * (self.count%count_cells_in_row)
        else:
            return '*****\n' * (self.count // count_cells_in_row - 1) + '*****'

org_cell1 = organic_cell(13)
org_cell2 = organic_cell(3)

# сложение двух клеток
org_cell_plus = org_cell1 + org_cell2
print (f'Результат сложения = {org_cell_plus.count}')
print(org_cell_plus.make_order(5))

# вычитание двух клеток
org_cell_minus = org_cell1 - org_cell2
print (f'Результат вычитания = {org_cell_minus.count}')
print(org_cell_minus.make_order(5))

# умножение двух клеток
org_cell_mult = org_cell1 * org_cell2
print (f'Результат умножения = {org_cell_mult.count}')
print(org_cell_mult.make_order(5))

# деление двух клеток
org_cell_devide = org_cell1 // org_cell2
print (f'Результат деления нацело = {org_cell_devide.count}')
print(org_cell_devide.make_order(5))

# деление двух клеток
#org_cell_devide2 = org_cell1 / org_cell2
#print (f'Результат деления = {org_cell_devide2.count}')
#print(org_cell_devide2.make_order(5))