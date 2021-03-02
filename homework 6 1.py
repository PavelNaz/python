from time import sleep


class TrafficLight:
    __color = ['red','yellow','green']

    def running(self):
        print('Светофор работает')

        self.__color = 'red'
        print(f'Сейчас цвет: {self.__color}')
        sleep(7)

        self.__color = 'yellow'
        print(f'Сейчас цвет: {self.__color}')
        sleep(2)

        self.__color = 'green'
        print(f'Сейчас цвет: {self.__color}')
        sleep(10)

        while True:
            self.running()


TrafficL = TrafficLight()
TrafficL.running()