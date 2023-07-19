# Int numbers------------------------------------------------

# вводимое пользователем число будет строкой
# input_str = input("Enter any number: ")
# input_int = int(input_str)  # конвертируем строку в число


# print(input_int)

# print(type(input_int))

# число которое нужно возвести в степень
# input_base = int(input("Enter 1st number: "))
# # степень в которую нужно возвести первое число
# input_power = int(input("Enter 2st number: "))


# # pow(a, b) функция возводит число а в степень b
# print(pow(input_base, input_power))
# # тип получившегося чилсла будет int
# print(type(pow(input_base, input_power)))


# большое число можно разделять на части нижним подчеркиванием для лучшей читаемости
# long_int = 1_000_000_000

# print(long_int)  # вывод будет 1000000000


# Float numbers-----------------------------------------------------

str_temperature = '20.5'
str_temperature1 = 11.4
str_temperature2 = 11.77

print(float(str_temperature))  # конвертируем строку в float
print(type(float(str_temperature)))  # <class 'float'>
print(int(str_temperature1))  # коневертируем float в int
print(type(int(str_temperature1)))  # <class 'int'>

# round() - округление числа с десятичной точкой до ближайшего целого числа
print(round(str_temperature1))  # 11
print(round(str_temperature2))  # 12
print(type(round(str_temperature1)))  # <class 'int'>


# Complex numbers------------------------------------------------------
# комплексные числа состоят из действительной и мнимой части

complex_a = 10 + 7j  # 10 - действительная часть, 7j - мнимая часть
complex_b = 3 + 3j

print(complex_a + complex_b)  # (13+10j)
print(complex_a - complex_b)  # (7+4j)
print(complex_a * complex_b)  # (9+51j)

# (10 + 7j)(3 + 3j) = (10*3) + (10*3j) + (7j*3) + (7j*3j)
# = 30 +30j + 21j +21j^2 = 30 +30j +21j - 21 = 9 + 51j
