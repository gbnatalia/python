'''
Реализовать проект "Операции над комплексными числами".
Создать класс "Комплексное число".
Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
выполнить сложение и умножение созданных экземпляров.
Проверить корректность полученного результата.
'''

class Complex_number:
    def __init__(self, real=0, im=0):
        self.real = real
        self.im = im

    def __str__(self):
        res = 0
        if self.real != 0 and self.im != 0:
            if self.im > 0:
                res = f'{self.real} + {self.im}i'
            else:
                res = f'{self.real} - {-self.im}i'
        elif self.im != 0:
            res = f'{self.im}i'
        else:
            res = f'{self.real}'
        return res

    def __add__(self, other):
        return Complex_number(self.real + other.real, self.im + other.im)

    def __mul__(self, other):
        return Complex_number(self.real * other.real - self.im * other.im,
                              self.real * other.im + self.im * other.real)

if __name__ == "__main__":
    cn1 = Complex_number(2, 3)
    print(cn1)
    cn2 = Complex_number(0, -3.5)
    print(cn2)
    print(f'сумма = {cn1 + cn2}')
    print(f'Произведение = {cn1 * cn2} ')
    cn3 = Complex_number(2.5)
    print(cn3)
    cn4 = Complex_number()
    print(cn4)




