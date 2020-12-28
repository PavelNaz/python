def div(*args):
    try:
        var_1 = int(input("Введите делимое "))
        var_2 = int(input("Введите делитель "))
        res = var_1 / var_2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Вы не можете делить на нуль"

    return res

print(f'{div()}')