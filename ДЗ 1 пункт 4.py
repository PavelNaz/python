number = int(input("Введите целое положительное число: "))

maximum = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > maximum:
        maximum = number % 10
    if number > 9:
        continue
    else:
        print("Максимальное цифра в числе: ", maximum)
    break
