number = input("Enter number: ")

x = 0
for y in number:
    while int(y) > x:
        x = int(y)
print(x)
