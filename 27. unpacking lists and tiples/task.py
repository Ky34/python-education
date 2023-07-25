
users_list = [{'name': 'Alesha', 'age': 23},
              {'name': 'Valeron', 'age': 33},
              {'name': 'Chel', 'age': 13}]

user_one, user_two, user_three = users_list


def user_info(name, age):
    return f"Its {name}, he is {age} years old"


print(user_one)
print(user_two)
print(user_three)

print(user_info(**user_one))
print(user_info(**user_two))
print(user_info(**user_three))
