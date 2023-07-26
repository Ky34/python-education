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
