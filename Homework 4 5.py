from functools import reduce


def func(el_p, el):
    return el_p * el

print(f'Список четных {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения {reduce(func, [el for el in range(99, 1001) if el % 2 == 0])}')