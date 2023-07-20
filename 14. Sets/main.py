# Sets - множества(наборы)
# Множество - это неупорядоченная последовательность элементов
# Множество содержит только уникальные элементы
# В множествах обычно сохраняют однотипные данные (объекты)

my_fruits = {'apple', 'banana', 'lime'}
other_fruits = {'banana', 'lime', 'apple'}
posts_ids = {151, 245, 762, 167}
# В множества можно добавлять элементы разных типов, но зачастую так не делают
user_inputs = {True, 'hi', 10, 5, 11}
print(my_fruits)
print(type(my_fruits))

# создавать множества с одиннаковыми элементами можно
posts_ids_1 = {151, 245, 167, 167, 151}
# но при выводе они будут автоматически удалены:
print(posts_ids_1)  # {151, 245, 167}

# Порядок в множествах не важен

print(my_fruits == other_fruits)  # True

print(len(my_fruits))  # 3
print(len(user_inputs))  # 5

# у элементов множеств нет индексов,
# поэтому получить значение по индексу в множестве нельзя


# Изменяемые объекты в множествах:
# в множества нельзя добавлять изменяемые объекты,
# такие как list, dict, set

# lists_set = {[1, 2], [3, 7]}  # TypeError: unhashable type: 'list'

# так же в множествах нельзя использовать оператор del для удаления элемента


# Методы множеств

photo_sizes = {'1920x1080', '800x600'}
other_sizes = {'800x600', '480x640'}

photo_sizes.add('1024x768')  # добавление элементов
print(photo_sizes)  # {'1024x768', '1920x1080', '800x600'}


# .union() - объединение множеств
# можно использовать оператор - |
all_sizes = photo_sizes.union(other_sizes)
all_sizes = photo_sizes | other_sizes
print(all_sizes)  # '1920x1080', '1024x768', '800x600', '480x640'}

# .intersection() - метон находит пересечение двух множеств
# можно использовать оператор - &
common_sizes = photo_sizes.intersection(other_sizes)
common_sizes = photo_sizes & other_sizes
print(common_sizes)  # общие элементы из 2ух множеств {'800x600'}

# .issubset() - проверяет включено ли одно множество в другое
nums = {10, 5, 35}
other_nums = {20, 5, 12, 10, 35}
# проверяем, включено ли множетво nums в множество other_nums
res = nums.issubset(other_nums)
print(res)  # True все элементы первого множества включены во второе

# .issuperset() так же можно проверить включено ли nums в other_nums
res = other_nums.issuperset(nums)
print(res)  # True
