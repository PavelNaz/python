def my_func (val_1, val_2, val_3):
    if val_1 >= val_3 and val_2 >= val_3:
        return val_1 + val_2
    elif val_1 > val_2 and val_1 < val_3:
        return val_1 + val_3
    else:
        return val_2 + val_3

print(f'Result - {my_func(int(input("Первый аргумент ")), int(input("Второй аргумент ")), int(input("Третий аргумент ")))}')