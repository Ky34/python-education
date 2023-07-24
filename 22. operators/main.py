# Операторы и операнды

a = 10
b = a
c = a + b

# Совпадают ли ссылки на объект
print(a is b)  # True
print(c is a)  # False


a = [1, 2]
b = [1, 2]

print(a == b)  # True
print(a.__eq__(b))  # True
print(a.__eq__)  # <method-wrapper '__eq__' of list object at 0x7fe88b3f87c0>

print(id(a) == id(b))  # False
print(id(a))
print(hex(id(a)))


# Бинарные и унарные операторы

# Унарные операторы всегда имеют один операнд

# - my_number  # используется чтобы поменять знак
# + my_number
# not is_activated  # логический оператор отрицания

my_num = 10
my_bool = True

# используя унарный оператор + мы явно показывает что переменная является числом
print(+my_num)  # 10
print(+my_bool)  # 1 - таким образом конвертируем True  в целое число

# отрицание правдивого значения - False
# отрицание ложного значения - True
print(not my_num)  # False


# Бинарные операторы
# a = 5
# a + b
# a += 5
# a == b
# a and b

# Инфиксная запись - когда оператор находится между 2мя операндами
# a = True
# a + b
# a > b
# a or b
print('========================================================')

# Операторы in, not in

my_car = {
    'brand': 'Toyota',
    'price': 10_000
}

print('brand' in my_car)  # True
print('year' in my_car)  # False
print('year' not in my_car)  # True


# Приоритетность операторов

# a + b * c / d - e
# a + ((b * c) / (d - e))


# Ложные значения
# значение, которое при приведении к логическому типу
# дает False является ложным
# int 0
# float 0.0
# complex 0j
# bool False
# NoneType None
# Ложными являются пустые значения всех последовательностей
# dict {}
# list []
# tuple ()
# set set()
# range range(0)
# str ""


print(bool(0))  # False
print(bool(0.0))  # False
print(bool(0j))  # False
print(bool(False))  # False
print(bool(None))  # False
print(bool({}))  # False
print(bool([]))  # False
print(bool(()))  # False
print(bool(set()))  # False
print(bool(range(0)))  # False
print(bool(""))  # False
print(not not {})
print(not not ())
print(not not [1, 2, 3])

my_list = [1, 2]

if len(my_list) > 0:
    print("List has elements")

if len(my_list):
    print("List has elements")
print('==============================================================')


# Логические операторы
# not/and/or

not 10  # False
not 0  # True
not 'abc'  # False
not ''  # True
not True  # False
not None  # True

not not 10  # True
not not 0  # False
not not 'abc'  # True
not not ''  # False
not not True  # True
not not None  # False

# операторы короткого замыкания or\and

my_list = [1, 2]
other_list = ['a', 'b']
my_dict = {}

# выражение с оператором or возвращает первое правдивое значение
print(my_list or other_list)  # [1, 2]
print(len(my_list) > 0 or other_list)  # True
print(len(my_list) < 0 or other_list)  # ['a', 'b']

# выражение с оператором and возвращает первое значение если оно ложно
# если первое значение правдиво, то возвращается второе значение независимо
# от того, ложно оно или правдиво

print(my_list and my_dict)  # {}
print(bool(my_list and my_dict))  # False


my_list and print("List is not empty")

new_dict = {
    'kekw': 'lul',
    'lul': 'kekw'
}

other_dict = {
    'kekw': 'lul',
    'lul': 'kekw'
}

new_dict == other_dict and print("Словари одинаковы")
