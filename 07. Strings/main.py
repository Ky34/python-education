# Strings

long_str = "This is a very long string"
long_str = """This is 
a very 
long string"""

print(long_str)

print(type(long_str))  # class 'str'
print(type(str))  # class 'type'
print(type(int))  # class 'type'
print('-----', id(long_str))

# Strings methods and functions
# Методы, наследуемые всеми экземплярами строк:
# upper() replace() count() index() capitalize() lower() ...

my_comment = "This is my short comment"

print(len(my_comment))  # возвращает длинну строки

# заменяем слово 'short' на слово 'long', исходная строка не изменяется
print(my_comment.replace('short', 'long'))

# считает колличество символов указанных в скобках
print(my_comment.count(' '))
# считает колличество символов или подстрок указанных в скобках
print(my_comment.count('is'))

print(my_comment[0])  # вернет элемент из строки с индексом 0
print(my_comment[-1])  # первый символ с конца
print(my_comment[-5])
print(my_comment[2:7])  # возвращает строку в диапозоне от 2 символа до 6
print(my_comment[8:])  # вернет строку с 8 символа и до конца
print(my_comment[:10])  # вернет строку с 0 символа до 9
