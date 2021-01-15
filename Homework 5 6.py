subjects = {}

try:
    with open("text_6.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        data = line.replace(' ', ' ').split()

        subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
except ValueError:
    print("Неправильные данные")

print(subjects)
