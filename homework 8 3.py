class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                value = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(value)
                print(f'Список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                yes_or_no = input(f'Попробовать еще раз? Y/N ')

                if yes_or_no == 'Y' or yes_or_no == 'y':
                    print(try_except.my_input())
                elif yes_or_no == 'N' or yes_or_no == 'n':
                    return f'Выход из программы'
                else:
                    return f'Выход из программы'

try_except = Error(1)
print(try_except.my_input())