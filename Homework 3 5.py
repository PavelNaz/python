def sum_values():
    sum = 0.0
    while True:
        key = input("Ввести число (да / нет) ? ")
        if key.lower() == "нет":
            return sum
        else:
            for i in input("Введите числа через пробелы: ").split():
                try:
                    sum += float(i)
                except ValueError:
                    return sum
print(f"Сумма: {sum_values()}")