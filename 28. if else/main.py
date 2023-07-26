# if

my_number = 25

if my_number > 0:
    print(my_number, "is pos num")

person_info = {
    'age': 20
}


if not person_info.get('name'):
    # Действия в случая, если:
    # 1. Ключа "name" у объекта "person_info" нет
    # 2. Ключ "name" есть, но его значение ложно
    print("Имя отсутствует")


num_one = 10
num_two = 5

if (num_one > 0 and
    num_two > 0 and
    # проверяем принадлежат ли числа классу int
    isinstance(num_one, int) and
        isinstance(num_two, int)):
    print("Both numbers are ints and positive")


# if else

my_number = 21.5

if type(my_number) is int:
    print(my_number, "is integer")
else:
    print(my_number, "is not an integer")


my_phone = {
    'price': 200
}

if my_phone.get('brand'):
    print("Phone's brand is", my_phone['brand'])
else:
    print("There is no phone brand")


# if elif

my_number = -10

if my_number > 0:
    print(my_number, "is positive number")
elif my_number < 0:
    print(my_number, "is negative number")
else:
    print(my_number, "is zero")


# if in func

def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        info = "Один из аргументов не целое число"
    elif a >= b:
        info = f"{a} больше или равно {b}"
    else:
        info = f"{a} меньше {b}"
    return info


def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        return "Один из аргументов не целое число"
    if a >= b:
        return f"{a} больше или равно {b}"
    return f"{a} меньше {b}"


print(nums_info(True, 10))
print(nums_info(2, 10))
print(nums_info(20, 10))
