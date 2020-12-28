from itertools import count

for el in count(int(input('Стартовое число '))):
    if el > 20:
        break
    print(el)
