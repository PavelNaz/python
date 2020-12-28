def func(x, y):
    return 1 / x ** abs(y)
print(f'Result {func(int(input("Первый аргумент ")), int(input("Второй аргумент ")))}')

def func_1(x, y):
    for i in range(-y):
        x *= 1 / x
    return x
print(f'Result {func(int(input("Первый аргумент ")), int(input("Второй аргумент ")))}')
