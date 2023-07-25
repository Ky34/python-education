# присвоение значений из списка переменным

my_fruits = ['apple', 'banana', 'lime']
other_fruits = ('apple', 'banana', 'lime')

# распаковка списка и кортежа. порядок следования важен
my_apple, my_banana, my_lime = my_fruits
other_apple, other_banana, other_lime = other_fruits

print(my_apple)
print(my_banana)
print(my_lime)

print(other_apple)
print(other_banana)
print(other_lime)

# использование * при распаковке

my_apple, *remaining_fruits = my_fruits

print(my_apple)
print(remaining_fruits)  # ['banana', 'lime']
print('==========================================')

# Распаковка словаря в именованные аргументы

user_profile = {
    'name': 'Alesha',
    'comments_qty': 23
}


def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


print(user_info(user_profile['name'], user_profile['comments_qty']))
# распаковываем словарь в вызове функции
print(user_info(**user_profile))


# распаковка списка в позиционные аргументы

user_data = ['Alesha', 23]

# при этом в списке должно быть 2 элемента


def user_info(name, comments_qty):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


print(user_info(*user_data))
