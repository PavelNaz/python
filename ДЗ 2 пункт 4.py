str = input("Ввести строку: ")
x = str.split(' ')
for x, el in enumerate(x,1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{x} - {el}")