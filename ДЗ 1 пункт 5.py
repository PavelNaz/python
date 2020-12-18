profit = float(input('Выручка фирмы: '))
costs = float(input('Издержки фирмы: '))
person = int(input('Количество рабочих'))

if profit>costs:
    print(f"Прибыль положительная. Рентабельность составляет {profit/costs} рублей")
    print(f'Прибыль фирмы на одного сотрудника составляет {profit/person} рублей')
elif profit==costs:
    print('Нулевая выручка')
else:
    print('Убыток')