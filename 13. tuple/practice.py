my_nums = (10, 5, 5, 100, 5, 0, 5, 5)

print(my_nums.count(5))  # 3
print(my_nums.index(5))  # 1

# чтобы найти индекс последующих элементов со значением 5
index_one = my_nums.index(5)  # присваиваем индекс первого элемента переменной
# в скобках после значения элемента, который нужно искать указываем индекс с которого нужно начать
# добваляем еденицу так как поиск начинается включительно с указанного индекса элемента
index_two = my_nums.index(5, index_one + 1)  #
# так находим индекс 3-го элемента
index_three = my_nums.index(5, index_two + 1)  #

print(index_two)  # 2
print(index_three)  # 4

# for i in range(my_nums.count(5) - 1):
#     index_one = my_nums.index(5, index_one + 1)
#     print(index_one)

my_list = list(my_nums)
my_list.append(7)

print(my_list)
print(my_nums)

my_nums = tuple(my_list)

print(my_nums)


my_tuple = tuple('abcd')

print(my_tuple)  # ('a', 'b', 'c', 'd')

my_new_tuple = tuple({'first': 1, 'second': 2})

print(my_new_tuple)  # ('first', 'second')


my_other_types = (10, 10.4, 'coocoo', True)
my_another_types = (10.3, 'loshadi', [1, 2, 4], True)

my_total_tuple = my_other_types + my_another_types

print(my_total_tuple)
