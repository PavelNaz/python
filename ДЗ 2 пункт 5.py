number = int(input("Напишите число: "))
list = [7, 5, 3, 3, 2]
x = list.count(number)
for el in list:
    if x > 0:
        a = list.index(number)
        list.insert(a + x, number)
        break
    else:
        if number > el:
            b = list.index(el)
            list.insert(b, number)
            break
        elif number < list[len(list) - 1]:
            list.append(number)
print(list)


