# 1.

def merge_lists_to_dict(list_one, list_two):
    zip_lists = zip(list_one, list_two)
    return dict(zip_lists)


my_list = ['name', 'last_name', 'age']
other_list = ['Alesha', 'Kozlov', 33]

my_dict = merge_lists_to_dict(my_list, other_list)
print(my_dict)

car_list = ['Audi', 'BMW', 'Honda']
model_list = ['A8', 'X6', 'Accord']
cars_dict = merge_lists_to_dict(car_list, model_list)

print(cars_dict)

print('===================================================')

# решение


# def merge_list_to_dict_one(list_one, list_two):
#     zipped_seq = zip(list_one, list_two)
#     return dict(zipped_seq)

def merge_list_to_dict_one(list_one, list_two):
    return dict(zip(list_one, list_two))


res_one = merge_list_to_dict_one(['a', 'b', 'c'], [10, True, []])
print(res_one)

res_two = merge_list_to_dict_one(['abc'], [{}, True, 100])
print(res_two)

# в словаре ключ не может быть пустым словарем
# res_three = merge_list_to_dict_one([{}, True, 100], ['abc'])  # TypeError: unhashable type: 'dict'
# TypeError: unhashable type: 'dict'

res_three = merge_list_to_dict_one([10, True, 100], ['abc'])
print(res_three)
