for el in [1, 'abc', True]:
    print(type(el))
    print(el)

my_dict = {'id': 324, 'title': 'test'}

for key in my_dict:
    print(type(key))
    print(key)
    print(key, my_dict[key])
print('=====================================================')

# for in для словарей и метод items()

my_object = {
    'x': 10,
    'y': True
}

# метод items() возвращает пары ключ значение в виде кортежа
for key, value in my_object.items():
    print(key, value)


# Цикл for in для множеств

video_ids = {1456, 1233, 5773, 8990}

for id in video_ids:
    print(id)


# Встроенная функция filter()

def filter_list(list_to_filter, value_type):
    # def check_element_type(elem):
    #     return type(elem) is value_type
    return list(filter(lambda elem: type(elem) is value_type,
                       list_to_filter))


res = filter_list([1, 10, 'abc', 5.5], float)

print(res)
