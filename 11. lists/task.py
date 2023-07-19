# Task 1

# 1. Создайте список с 5 элементами разных типов:

my_list = [7, 5.5, 'Alesha', True, {'age': 12, 'name': 'Valera'}]
my_new_list = ['abc', 5, 10.5, True, [1]]


# 2. Удалите 3-ий элемент

my_list.pop(2)
print(my_list)
my_new_list.pop(2)
print(my_new_list)


# 3. Выведите в терминал длинну списка

print(len(my_list))
print(len(my_new_list))


# 4. Поменяйте порядок следования элементов в списке

my_list.reverse()
print(my_list)
my_new_list.reverse()
print(my_new_list)


# 5. Создайте еще один список с 2-я элементами

new_list = [113, False]
my_other_list = [True, {'a': 10}]


# 6. Расширте первый список элементами второго

my_list.extend(new_list)  # добавляем в список элементы 2-го списка
my_new_list.extend(my_other_list)
print(my_other_list)

# 7.

print(my_list)
print(my_new_list)

print('====================================================================')

# Task 2

# 1. Создайте 2 списка

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# 2. Объедените 2 списка используя +

new_list = list1 + list2

# 3.

print(new_list)
print(list1.__add__(list2))


first_list = [10, True, 'abc']
second_list = [[1, 2], {'b': True}]

merged_list = first_list + second_list
print(merged_list)

other_merged_list = first_list.__add__(second_list)
print(other_merged_list)
