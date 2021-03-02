from math import factorial
from itertools import count

def generator():
    for el in count(int(input('Стартовое число '))):
        yield factorial(el)

gen = generator()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break