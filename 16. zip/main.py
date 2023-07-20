# Встроенная функция zip()

fruits = ['apple', 'banana', 'lime', 'orange']
quantities = [100, 70, 50, 20]

# с помощью функции zip() можно выполнить слияние двух списков
# попарно в соответствии с индексами
fruits_qtys_zip = zip(fruits, quantities)

print(fruits_qtys_zip)  # <zip object at 0x7f9b4d08adc0>
print(type(fruits_qtys_zip))

# zip объект можно конвертировать в список и получить список кортежей

# [('apple', 100), ('banana', 70), ('lime', 50)]
fruits_qtys_list = list(fruits_qtys_zip)

print(fruits_qtys_list)

# если элементов в одном из списков больше,
# то они будут проигнорированы при конвертации.
# zip объект формируется на основании самого короткого из списков

availability = (True, False, False, True)

fruits_qtys_zip = zip(fruits, quantities, availability)
# получаем список из кортежей в каждом по 3 элемента
print(list(fruits_qtys_zip))
print('-----------------------------------------------------------------')

# Конвертация zip в словарь
# при конвертации zip в словарь,
# допускается только 2 объекта в вызове функции zip
# в первой будут ключи а во второй значения

fruits_qtys_zip = zip(fruits, quantities)

# {'apple': 100, 'banana': 70, 'lime': 50, 'orange': 20}
fruits_qtys_dict = dict(fruits_qtys_zip)

print(fruits_qtys_dict)

# Task

products = ['salt', 'pepper', 'sugar', 'carry']
prices = [100, 200, 500, 150]

zip_prices = zip(products, prices)
zip_prices = zip(products, prices)


prices_dict = dict(zip_prices)
print(prices_dict)


zip_prices = zip(products, prices)
prices_list = list(zip_prices)
print(prices_list)
