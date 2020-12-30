with open('text_3.txt', 'r') as my_file:
    salary = []
    poor_worker = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor_worker.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20.000 {poor_worker}, средний оклад {sum(map(int, salary)) / len(salary)}')



