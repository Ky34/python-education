# 1.

my_cars = {
    'first': 'honda',
    'second': 'audi',
    'third': 'pegeout'
}

my_capitalizevelues_cars = {k: v.upper() for k, v in my_cars.items()}

print(my_capitalizevelues_cars)

# 2.

my_list = ['asdasd', 'zx', 'qwee', 'aaaaqeeqw', 'a']

new_list = [string for string in my_list if len(string) > 3]

print(new_list)
