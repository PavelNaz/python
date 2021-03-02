class Stationery:
    atr_title = 'Title'
    def draw(self):
        print('Программа зарисовки запущена')
class Pen(Stationery):
    def draw(self):
        print('Зарисовка ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Зарисовка карандашом')
class Handle(Stationery):
    def draw(self):
        print('Зарисовка маркером')

my_stationery = Stationery()
my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_stationery.draw()
my_pen.draw()
my_pencil.draw()
my_handle.draw()