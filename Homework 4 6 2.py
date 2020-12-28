from itertools import cycle

my_list = ['ABC', 123]
x = 0
for el in cycle(my_list):
    if x >= 6:
        break
    print(el)
    x += 1