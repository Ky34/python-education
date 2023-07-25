# TRY / EXCEPT

try:
    # выполнение блока кода
    pass
except ErrorType:  # <- тип ошибки
    # этот код выполняется в случае возникновения ошибок в блоке try
    pass

try:
    print(10 / 0)
# если возникает ошибка ZeroDivisionError
except ZeroDivisionError:
    print(ZeroDivisionError)
    print("Error - Division by zero!")


print('Continue...-----------------------------------------------------')


# Получение информации об ошибке

try:
    print(10 / 0)
except ZeroDivisionError as e:
    # переменная е будет содержать информацию об ошибке
    print(type(e))
    # print(dir(e))
    print(e)


# другие типы ошибок

try:
    print('10' / 0)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

print('Continue...-----------------------------------------------------')


# блоки else и finally

# блок else
try:
    print(10 / 5)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
# если в блоке try не возникла ни одна из указанных ошибок,
# то выполнится блок else
else:
    print("There was no error")

# блок finally

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("There was no error")
# блок finally выполняется в любом случае, не зависимо от того возникла ошибка или нет
finally:
    print('Continue...-----------------------------------------------------')


# любые ошибки в блоке except

# универсальный подход к обработке ошибок
try:
    print(10 / 0)
except Exception as e:
    print(e)

# не рекомендуется использовать такой вариант
try:
    print(10 / 0)
except:
    print("Some error occurred")

print('------------------------------------------')

# создание ошибок


def divide_nums(a, b):
    if b == 0:
        # создаем экземпляр класса ValueError с текстом
        raise ValueError("Second arguument can't be 0")
    return a / b


# ошибка ZeroDivisionError больше не возникает, так как мы обработали тип ошибки внутри функции
try:
    divide_nums(10, 0)
# except ZeroDivisionError as e:
#     print(e)
except ValueError as e:
    print(e)

print('Continue...-----------------------------------------------------')
