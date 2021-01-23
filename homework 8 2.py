class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        num_1 = int(input('Введите делимое: '))
        num_2 = int(input('Введите делитель: '))
        if num_2 == 0:
            raise Error("Деление на нуль запрещается!")
        else:
            result = num_1 / num_2
            return result
    except ValueError:
        return "Вы ввели не число"
    except Error as error:
        return error


print(div())