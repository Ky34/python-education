# Task 1.

user_one = {
    'age': 10,
    'weight': 100
}

user_two = {
    'age': 17,
    'weight': '77.1'
}

user_three = {
    'age': 23.5,
    'weight': 'tall'
}

# мое решение


def dict_to_list(dict_to_convert):
    users = list()
    for user in dict_to_convert.items():
        if type(user[1]) == int:
            user_list = list(user)
            user_list.append(user_list.pop(1) * 2)
            users.append(tuple(user_list))
        else:
            users.append(user)
    return users

# решение на курсе


def dict_to_list(dict_to_convert):
    list_for_convertion = []
    for k, v in dict_to_convert.items():
        if type(v) == int:
            v *= 2
        list_for_convertion.append((k, v))
    return list_for_convertion


print(dict_to_list({'a': 5, 'b': [], 'c': 100}))

print(dict_to_list(user_one))
print(dict_to_list(user_two))
print(dict_to_list(user_three))
print('==========================================================')


# Task 2.

def filter_list(list_to_filter, value_type):
    filtred_list = []
    for element in list_to_filter:
        if type(element) == value_type:
            filtred_list.append(element)
    return filtred_list


def filter_list(list_to_filter, value_type):
    filtred_list = []
    for element in list_to_filter:
        if type(element) == value_type:
            filtred_list.append(element)
        # Not recommended, because bool is subclass of int
        # if isinstance(element, value_type):
        #     filtred_list.append(element)
    return filtred_list

# def filter_list(lis, typ):
#     filtred_list = []
#     for element in lis:
#         if type(element) == typ:
#             filtred_list.append(element)
#     return filtred_list


print(filter_list(['strind', 'strip', 11, 10, 9, True], str))
print(filter_list(['strind', 'strip', 11, 10, 9, True], int))
print(filter_list(['strind', 'strip', 11, 10, 9, True], bool))
# print(filter_list(['strind', 'strip', 11, 10, 9, True], None))
