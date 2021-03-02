lesson-2
number = input("Enter number: ")

x = 0
for y in number:
    while int(y) > x:
        x = int(y)
print(x)

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

