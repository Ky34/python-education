# Встроенный в Python функции

# print('Hello Python')
# type()
# id()
# len()
# sum()
# input()
# round()
# min()
# max()
# int()
# str()
# bool()
# и другие

# print(print)

# name = 'Alesha'
# print(10, 'Alesha', True)
# print(dir(__builtins__)) # весь список встроенных в Python функций
# print(dir(name))  # функция dir() отображает имена всех атрибутов объекта
# print(name.upper())  # вызываем метод .upper() для переменной name
# name = input('Enter your name:')

name = input('Enter your name: ')
# age = input('Enter your age: ')
# city = input('Enter you city: ')
# print(
#     f'Здравствуйте {name}, а вы уже взрослый раз вам {age} лет, как дела у вас в {city}')

print(name.capitalize())  # метод capitalize() пишет все слова с заглавной буквы
print(name.upper())
print(name.lower())
print(dir(name))
