my_disk = {}

print(id(my_disk))
print(type(my_disk))

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80

print(my_disk)

# при использовании метода .items() возвращается список
# с парами ключ: значение в виде кортежей
print(my_disk.items())
print(type(my_disk.items()))

print(list(my_disk.keys()))  # список ключей словаря
print(my_disk.popitem())  # .popitem() удаляет последний добавленный ключ
print(my_disk)

print(my_disk.get('type', 'hdd'))

print(my_disk.copy())  # создается новый объект на основании предыдущего

new_disc = my_disk.copy()
new_disc['type'] = 'ssd'

print(len(new_disc))

# Конвертация других значений в словарь

# словарь можно создать из списка списков и списка кортежей
my_list = [['first', 0], ['second', True]]
my_list1 = [('first', 0), ('second', True)]

my_dict = dict(my_list)
my_dict1 = dict(my_list1)

print(my_dict)
print(my_dict1)
