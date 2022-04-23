'''
4. Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
'''

class Car:
    '''    Класс характеристик машин    '''

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина поворачивает {direction}")

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение допустимой скорости в 60 км/ч. Текущая скорость = {self.speed}')
        else:
            print(f'Текущая скорость = {self.speed}')

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение допустимой скорости в 40 км/ч. Текущая скорость = {self.speed}')
        else:
            print(f'Текущая скорость = {self.speed}')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


if __name__ == "__main__":
    print("\nГородская машина:")
    tc = TownCar(70, "red", "lada")
    print(f"Аттрибуты -  Скорость: {tc.speed}, Цвет: {tc.color}, Имя: {tc.name}, Машина поицейская?: {tc.is_police} ")
    tc.go()
    tc.show_speed()
    tc.turn("направо")
    tc.stop()

    print("\nРабочая машина:")
    wc = WorkCar(30, "black", "ford")
    print(f"Аттрибуты -  Скорость: {wc.speed}, Цвет: {wc.color}, Имя: {wc.name}, Машина поицейская?: {wc.is_police} ")
    wc.show_speed()

    print("\nСпортивная машина:")
    sc = SportCar(130, "black", "ford")
    print(f"Аттрибуты -  Скорость: {sc.speed}, Цвет: {sc.color}, Имя: {sc.name}, Машина поицейская?: {sc.is_police} ")
    sc.show_speed()

    print("\nПолицейская машина:")
    pc = PoliceCar(70, "black", "ford")
    print(f"Аттрибуты -  Скорость: {pc.speed}, Цвет: {pc.color}, Имя: {pc.name}, Машина поицейская?: {pc.is_police} ")
    pc.show_speed()
