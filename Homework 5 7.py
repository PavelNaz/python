import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('text_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, losses = line.split()
        profit[name] = int(earning) - int(losses)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Average profit - {prof_aver:.2f}')
    else:
        print(f'Average profit is negative. Losses')
    pr = {'average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Profit of each unit - {profit}')

with open('TEXT_file_7.json', 'w') as js:
    json.dump(profit, js)

    js_str = json.dumps(profit)
    print(f' Json file with the next details: \n '
          f' {js_str}')
