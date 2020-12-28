my_list = [1, 123, 545, 9, 9, 0, 100, 949, 88, 848]
my_new_list = [el for num, el in enumerate(my_list) if el > my_list[my_list.index(el)-1]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')