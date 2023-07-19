# Dict

my_motorbike = {
    'brand': 'Honda',
    'price': 10000,
    'engine_vol': 1.2
}

my_motorbike['price'] = 7000  # изменение значения
print(my_motorbike)

my_motorbike['is_new'] = True  # добавление нового ключа со значением True
print(my_motorbike)

del my_motorbike['price']  # удаление ключа
print(my_motorbike)


# Использование переменных в словарях

my_motorbike = {
    'brand': 'Honda',
    'price': 10000,
    'engine_vol': 1.2
}

key_name = 'brand'
my_motorbike[key_name] = 'BMW'
print(my_motorbike)  # {'brand': 'BMW', 'price': 10000, 'engine_vol': 1.2}

my_motorbike = {
    'brand': 'Honda',
    'engine_vol': 1.2,
    'price_info': {
        'price': 25000,
        'is_available': True
    }
}
# Для получения доступа к значениям вложенного словаря
# используется следующай запись:
print(my_motorbike['price_info']['price'])  # 25000
print(my_motorbike['price_info']['is_available'])  # True

# переменные можно использовать для создания словаря:
brand = 'Ducatti'
bike_price = 25000
engine_volume = 1.2

my_motorbike = {
    'brand': brand,
    'price': bike_price,
    'engine_volume': engine_volume
}
print(my_motorbike)

# длинна словаря

print(len(my_motorbike))
del my_motorbike['price']
print(len(my_motorbike))

# несуществующие ключи и метод get()
# если не уверены, есть ли ключ или нет в словаре,
# нужно использовать метод get()
print(my_motorbike.get('model'))  # если ключа в словаре нет, вернет None
print(my_motorbike.get('brand'))  # если ключ есть, вернет значение этого ключа

# можно присвоить значение по умолчанию для ключа, и если ключа в словаре нет, то метод вернет его
print(my_motorbike.get('qty', 0))  # 0
