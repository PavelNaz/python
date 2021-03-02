def summary():
    try:
        with open('text_5.txt', 'w+') as file:
            line = input('Введите цифры через пробел \n')
            file.writelines(line)
            number = line.split()

            print(sum(map(int, number)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()