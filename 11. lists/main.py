# Lists - списки

# В списках могут быть объекты разных типов.
# Порядок элементов в списках имеет значение,
# каждый элемент имеет свой уникальный индекс

posts_ids = [151, 245, 762, 167]
posts_ids[0] = 555  # заменяет элемент под индексом [0] на 555
posts_ids[2] = 333  # заменяет элемент под индексом [2] на 333
print(posts_ids)  # [555, 245, 333, 167]

del posts_ids[1]  # удаляет из списка элемент под индексом [1]
print(posts_ids)  # [555, 333, 167]
print(len(posts_ids))  # длинна списка измениться на 3
del posts_ids[-1]
print(posts_ids)  # удаляет из списка последний элемент
print('=============Список словарей========================')


# Список словарей:
users = [
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
]
print(len(users))  # 2
print(users[1]['user_id'])  # 831
print('=======Использование переменных при формировании списков=========')

# Использование переменных при формировании списков
my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruits = [my_fruit, other_fruit, new_fruit]
print(all_fruits)  # ['apple', 'banana', 'lime']
print('===============Методы списков========================')

# Методы списков

happy_smiles = []

happy_smiles.append(':)')  # .append() добавление новых элементов
happy_smiles.append(':*')  # элементы добавляются в конец списка
happy_smiles.append(':P')
happy_smiles.append(':B')
print(happy_smiles)
print(len(happy_smiles))
happy_smiles.pop()  # .pop() удаляет последний элемент из списка
happy_smiles.pop(0)  # удаляет элемент с индексом [0]
print(happy_smiles)
# метод .pop() возвращает элемент который был удален
removed_element = happy_smiles.pop()
print(removed_element)  # :P

print(happy_smiles)

posts_ids = [151, 245, 762, 167]
posts_ids.sort()  # по умолчанию сортирует список по возростанию
print(posts_ids)  # [151, 167, 245, 762]
posts_ids.sort(reverse=True)  # сортирует элементы по убыванию
print(posts_ids)  # [762, 245, 167, 151]
print('=============Разные операции со списками======================')


# Разные операции со списками

greeting = "Hello from Python"
greeting_letters = list(greeting)  # конвертируем строку в список

print(greeting_letters)

my_dict = {'a': 10, 'b': True}
# конвертируем словарь в список, в списке будут только ключи
my_dict_keys = list(my_dict)
print(my_dict_keys)  # ['a', 'b']

ratings = [2.5, 5.0, 4.3, 3.7]
other_ratings = [4.9, 3.4, 9.1]

print(min(ratings))  # минимальное значение в последовательности
print(max(ratings))  # максимальное значение в последовательности
print(sum(ratings))  # сумма элементов в списке

print(sum(ratings)/len(ratings))  # среднее значение

all_ratings = ratings + other_ratings  # можно объеденить списки
print(all_ratings)

first_two_ratings = ratings[:2]  # первые 2 элемента списка
print(first_two_ratings)

# получаем список начиная с [1] элемента до [-1] не включая его
middle_ratings = ratings[1: -1]
print(middle_ratings)

last_two_ratings = ratings[-2:]  # получаем последние 2 элемнта из списка
print(last_two_ratings)
print('==================Копирование списков============================')


# Копирование списков

my_cars = ['BMW', 'Mercedes']

# копирование по ссылке:
# новый объект не создаеться, создается ссылка, указывающая на старый объект
copied_cars = my_cars
copied_cars.append('Audi')
print(copied_cars)  # ['BMW', 'Mercedes', 'Audi']
print(my_cars)  # ['BMW', 'Mercedes', 'Audi']
print(id(copied_cars) == id(my_cars))  # True

# чтобы создать новый список и скопировать в него все элементы
# можно использовать несколько вариантов:


# 1:
my_cars = ['BMW', 'Mercedes']

# создается новый объект и в него записываются элементы списка
copied_cars = my_cars[:]  # копирование используя нарезку - slice
copied_cars.append('Audi')
print(copied_cars)
print(my_cars)
print(id(copied_cars) == id(my_cars))  # False


# 2:
my_cars = ['BMW', 'Mercedes']

# Копирование с использованием метода .copy()
copied_cars = my_cars.copy()
copied_cars.append('Audi')
print(copied_cars)
print(my_cars)
print(id(copied_cars) == id(my_cars))  # False


# 3:
my_cars = ['BMW', 'Mercedes']

# создание нового списка используя функцию list()
copied_cars = list(my_cars)
copied_cars.append('Audi')
print(copied_cars)
print(my_cars)
print(id(copied_cars) == id(my_cars))  # False
