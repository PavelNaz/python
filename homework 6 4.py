class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} начала свой путь.'

    def stop(self):
        return f'\n Машина {self.name} остановилась.'

    def turn(self, direction):
        return f'\n Машина {self.name} повернула {direction}'

    def show_speed(self):
        return f'\n Ваша скорость {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\n Вы превышаете скорость! Она сейчас составляет {self.speed}'
        else:
            return f'Скорость {self.name} допустима для продолжения пути'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\n Вы превышаете скорость! Она сейчас составляет {self.speed}'
        else:
            return f'Скорость {self.name} допустима для продолжения пути'


class PoliceCar(Car):
    pass

t = TownCar('Ауди', 70, 'черный', False)
print('1:\n' + t.go(), t.show_speed(), t.turn('налево'), t.turn('направо'), t.stop())

s = SportCar('Мерседес', 170, 'белый', False)
print('2:\n' + s.go(), s.show_speed(), s.turn('налево'), s.stop())

w = WorkCar('ВАЗ', 30, 'фиолетовый', False)
print('3:\n' + w.go(), w.show_speed(), w.turn('направо'), w.stop())

p = PoliceCar('КИА', 100, 'красный', True)
print('4:\n' + p.go(), p.show_speed(), p.turn('направо'), p.stop())