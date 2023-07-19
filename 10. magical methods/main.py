# Конвертация типов
# Python не выполняет неявную конвертацию типов
# 5 + '10' - error

# Встроенные функции для ЯВНОЙ конвертации типов
str()
float()
int()
list()
tuple()
set()
# ...

int_num1 = 5
float_num1 = 4.5
print(int_num1 + float_num1)
print(float_num1 + int_num1)

bool_val = True
int_val = 7
print(bool_val + int_val)
print(int_val + bool_val)
print('=================================================')


# Магические методы - это внутренние методы классов и они обычно не вызываются явно

int_num = 50
float_num = 7.5
str_val = 'abc'

# При выполнении математических операций Python вызывает магические методы:
# + - __add__ и __radd__, * - __mul__ и __rmul__ итд
# в названии магических методов 2 __ слева и справа
print(int_num * float_num)

# В магическом методе __mul__ для класса int не реализован
# функционал уножения целого числа на не целое число
print(int_num.__mul__(float_num))  # NotImplemented

# когда Python получает от магического метода результат NotImplemented
# он пытается вызвать магически метод для второго объекта __rmul__

print(float_num.__rmul__(int_num))  # 375

print(int_num * str_val)  # получаем новую строку где 50 раз повторяется 'abc'
print(str_val * int_num)  # получаем новую строку где 50 раз повторяется 'abc'

print(int_num.__mul__(str_val))  # NotImplemented
print(str_val.__rmul__(int_num))
print('=================================================================')

# можно просмотреть все методы класса bool и увидеть магические методы
print(dir(bool))
# можно просмотреть документацию, описывающую функцию bool()
print(bool.__doc__)
print(str.__doc__)


# функцией help() можно получить описание магического метода класса
print(help(list.__eq__))
