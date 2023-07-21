# Поведение неизменяемых объектов
# при присваивании одинаковых значений будут
# создаваться ссылки на один и тот же объект

from copy import deepcopy

my_number = 10
print(id(my_number))  # 140530460656144

other_number = 10
print(id(other_number))  # 140530460656144

print(id(10))  # 140530460656144
print('========================================')

first_num = 11
second_num = first_num

print(id(first_num))  # 140439572185648
print(id(second_num))  # 140439572185648
print('===========================================')
# при изменении создается новый объект в памяти
# исходный остается без изменений
second_num += 5
print(first_num)  # 11
print(second_num)  # 16
print(id(first_num))  # 140439572185648
print(id(second_num))  # 139697331372752

print('=========Поведение изменяемых объектов=========')
# Поведение изменяемых объектов:
# при присваивании одиннаковых значений,
# каждый раз будет создаваться новый объект в памяти
my_list = [1, 2, 3]
print(id(my_list))  # 139645687178304

other_list = [1, 2, 3]
print(id(other_list))  # 139645687255104

print(id([1, 2, 3]))  # 139645687178688
print('===============================================')

# изменения одного объекта не отражаются на другом
other_list.append(4)
print(my_list)  # [1, 2, 3]
print(other_list)  # [1, 2, 3, 4]


info = {
    'name': 'Alesha',
    'is_driver': False
}
info_copy = info  # в таком случае копируется ссылка на один и тот же объект
info['reviews_qty'] = 5

print(info['reviews_qty'])  # 5
print(info_copy['reviews_qty'])  # 5
print('========================================================')

# при создании словаря путем присваивания значения переменным,
# создаются 2 разных объекта в памяти

my_info = {
    'name': 'Alesha',
    'is_driver': False
}

other_info = {
    'name': 'Alesha',
    'is_driver': False
}

print(id(my_info))  # 140611055510720
print(id(other_info))  # 140611055557440

# при изменении одного словаря,
# изменения добавятся только в него
print('===========================================')

# как избежать измененй копий
# Вариант 1

info = {
    'name': 'Alesha',
    'is_driver': False
}

info_copy = info.copy()
info_copy['reviews_qty'] = 5

print(info)  # {'name': 'Alesha', 'is_driver': False}
print(info_copy)  # {'name': 'Alesha', 'is_driver': False, 'reviews_qty': 5}

# если в словаре у ключей есть изменяемые объекты,
# то ссылки копируются без изменений

info = {
    'name': 'Alesha',
    'is_driver': False,
    'reviews': []
}

info_copy = info.copy()
# при изменении значения в копии
info_copy['reviews'].append('Great driver!')
# изменения произойдут в обоих,
# так как вложенные изменяемые объекты сохраняются

# {'name': 'Alesha', 'is_driver': False, 'reviews': ['Great driver!']}
print(info)
# {'name': 'Alesha', 'is_driver': False, 'reviews': ['Great driver!']}
print(info_copy)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++=')

# чтобы создать полную копию объекта,
# можно воспользоваться встроенным в Python модулем copy

# from copy import deepcopy

info = {
    'name': 'Alesha',
    'is_driver': False,
    'reviews': []
}
info_deepcopy = deepcopy(info)
info_deepcopy['reviews'].append('Great driver!')

print(info)  # {'name': 'Alesha', 'is_driver': False, 'reviews': []}

# {'name': 'Alesha', 'is_driver': False, 'reviews': ['Great driver!']}
print(info_deepcopy)
