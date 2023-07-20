posts_ids = [10, 25, 16, 73]

# для списков метод __getitem__ определен поэтому
# мы можем обратиться к элементу по индексу
print(posts_ids.__getitem__(0))  # 10
print(posts_ids[0])  # 10

# для множеств маг метод __getitem__ не определен
# поэтому обратиться к элементу по индексу нельзя

posts_ids = {10, 25, 16, 73}

# print(posts_ids[0])  # TypeError: 'set' object is not subscriptable

# в множества можно добавзять кортежи, так как они неизменяемы
my_set = {(10, 10), 15, 5, 15}

print(my_set)
print(len(my_set))

# чтобы создать пустое множество, нужно возпользоваться функцией set()
new_set = set()
print(new_set)  # set()
print(type(new_set))  # <class 'set'>
print('------------------------------------------------------------')

# методы множеств

my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.intersection(other_set))
print(my_set.intersection('abc'))  # set()
print(my_set.intersection('abcd'))  # {'d'}
# можно передать список
print(my_set.intersection(['a', 'b', 'c', 'd']))  # {'d'}
# можно передать кортеж
print(my_set.intersection(('a', 'b', 'c', 'd')))  # {'d'}

print(my_set.union(other_set))  # {'abc', 'f', 'd', 'y', 'a'}
print(other_set.issubset(my_set))  # False
print(my_set.issubset(other_set))  # False
print(my_set.difference(other_set))  # {'abc', 'y'}
print(my_set - other_set)  # {'abc', 'y'}

# .discard() вернет исходное множетво,
# если попытаться удалить элемент которого в нем нет
my_set.discard('d')  # удаление элемента из множества
print(my_set)  # {'y', 'abc', 'f'}

# .remove() выдаст ошибку, если попытаться
# удалить элемент которого нет в множестве
# my_set.remove('def')  # KeyError: 'def'
print(my_set)

copied_set = my_set.copy()  # создает копию множества

my_set.add('t')
copied_set.add('l')

print(my_set & copied_set)  # {'abc', 'f', 'y'}

print(my_set)  # {'abc', 't', 'y', 'f'}
print(copied_set)  # {'abc', 'l', 'f', 'y'}


# симметричная разница в множествах
# метод .symmetric_difference возвращает элементы,
# которых нет в пересечении множеств
print(my_set.symmetric_difference(copied_set))  # {'t', 'l'}
print((my_set | copied_set) - (my_set & copied_set))  # {'l', 't'}
