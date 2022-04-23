'''
1. Создать класс TrafficLight (светофор):
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.
'''
import threading


class TrafficLight:
    '''       Класс "светофор"    '''

    colors = {
        'red':    "\033[31m",
        'yellow': "\033[33m",
        'green':  "\033[32m"
    }

    color_times = {
        'red':    7,
        'yellow': 2,
        'green':  4
    }

    def __init__(self, start_color='red'):
        if start_color in self.colors.keys():
            self.color = start_color
        print(f'{self.colors[self.color]}current color = {self.color}')

    def timeout(self):
        if self.color == 'red':
            self.color = 'yellow'
        elif self.color == 'yellow':
            self.color = 'green'
        else:
            self.color = 'red'
        print(f'{self.colors[self.color]}current color = {self.color}')

        tm = self.color_times[self.color]
        self.t = threading.Timer(tm, self.timeout)
        self.t.start()

    def running(self):
        tm = self.color_times[self.color]
        self.t = threading.Timer(tm, self.timeout)
        self.t.start()

if __name__ == "__main__":
    tl = TrafficLight()
    tl.running()
