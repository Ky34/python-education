# Документация функции
# Docstring - используется для документирования функций, классов, модулей

def mult_by_factor(value, mult=1):
    # описание функции должно находится в теле функции после
    # в самом начале после двоеточия в паре двойных кавычек "" ""
    ""'Multiplies number by multiplicator'""
    return value * mult


mult_by_factor(5)

# расширение которое автоматически добдавляет описание функции
# вызывается 3-мя парами двойных кавычек


def print_number_info(num):
    """
    prints num information

    Args:
        num (int): Integer number

    Returns:
        int: same number
    """
    if (num % 2) == 0:
        print('Num is even')
    else:
        print('Num is odd')
    return num


print_number_info(20)


# Область видимости переменных

a = 10


def my_fn():
    a = True
    b = 15
    # Python в первую очередь при вызове функции ищет переменную
    # в локальной области видимости
    print(a)  # True
    print(b)  # 15


my_fn()

print(a)  # 10

# переменная b создана в локальной области видимости функции
# поэтому в глобальной области она не видна
# print(b)  # NameError: name 'b' is not defined


# цепочка областей видимости

a = 5


def my_fn():
    def inner_fn():
        print(a)  # 5
    inner_fn()


my_fn()


# внутри функии можно создавать глобальную переменную

def my_fn():
    global a  # <- синтаксис
    a = 10  # переменная создается в момент присвоения значения


my_fn()  # после вызова функции переменная будет создана глобально
print(a)  # 10


#

def my_fn(c, d):
    print(c, d)
    print(dir())  # ['c', 'd']


my_fn('abc', 'xyz')

# так можно посмотреть переменные который были созданы в глобальной обласи видимости
print(dir())
