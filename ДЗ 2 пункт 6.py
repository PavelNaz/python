goods = []
while input("Вы желаете добавить продукт? ДА или НЕТ: ") == 'ДА':
    number = int(input("Вбейте номер продукта: "))
    features = {}
    while input("Вы желаете добавить наименование продукта? ДА или НЕТ: ") == 'ДА':
        feature_key = input("Вбейте наименование продукта: ")
        feature_value = input("Вбейте стоимость продукта: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)

analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(analitics)