def salary():
    try:
        time = float(input('Выработка в часах '))
        wage = int(input('Ставка в час в рублях '))
        bonus = int(input('Премия в рублях '))
        res = time * wage + bonus
        print(f'Заработная плата сотрудника в рублях равняется {res}')
    except ValueError:
        return print('Нужно писать все в цифрах')
salary()