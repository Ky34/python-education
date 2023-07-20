# tuple(кортеж) - упорядоченная последовательность элементов
# кортежи неизменяемые объекты
# порядок следования элементов в кортежах важен

some_tuple = (False, 'Alesha', 13)
my_fruits = ('apple', 'banana', 'lime')
other_fruits = ('lime', 'apple', 'banana', 'pineapple')

print(my_fruits == other_fruits)  # False

print(len(my_fruits))  # 3 длинна кортежа

# можно получать значение каждого элемента по id

print(other_fruits[1])  # apple
print(other_fruits[-1])  # pineapple
my_nums = (10, 5, 100, 0)

# my_fruits[0] = 'pineapple'  - изменять значения в кортежах нельзя
# del my_nums[1]  -  удалять элементы из кортежа нельзя

print(type(my_nums))

# Кортежи словарей\списков

users = (
    {
        'user_id': 133,
        'user_name': 'Alice'
    },
    {
        'user_id': 891,
        'user_name': 'Bob'
    }
)

print(users[1]['user_id'])  # 891

users[1]['user_id'] = 100  # изменяемые объекты в кортежах можно изменять

print(users[1]['user_id'])  # 100


# Использование переменных

my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruits = (my_fruit, other_fruit, new_fruit)
print(all_fruits)


# Объединение кортежей

internal_ids = (151, 100)
external_ids = (111, 839, 777)

# при использовании + вызывается метод кортежей __add__
all_ids = internal_ids + external_ids
print(all_ids)  # (151, 100, 111, 839, 777)


# Методы кортежей - .count() .index()

posts_ids = (151, 245, 762, 245)

# подсчет колличества элементов:
print(posts_ids.count(245))  # 2

print(posts_ids.count(151))  # 1

# поиск индекса элемента
print(posts_ids.index(762))  # индекс 2

# если элемент встречается несколько раз,
# то возвращается индекс первого элемента
print(posts_ids.index(245))  # индекс 1


# кортеж можно конвертировать в список,
# а список можно конвертировать обратно в кортеж

posts_ids_list = list(posts_ids)  # конвертируем в список
posts_ids_list.append(352)  # добавляем элемент
print(posts_ids_list)

posts_ids_tuple = tuple(posts_ids_list)  # конвертируем список обратно в кортеж
print(posts_ids_tuple)
