my_file = open("text_1.txt", "w")
line = input("Ввести данные \n")
while line:
    my_file.writelines(line)
    line = input('Ввести данные \n')
    if not line:
        break

my_file.close()

my_file = open('text_1.txt', 'r')
content = my_file.readlines()
print(content)

my_file.close()
