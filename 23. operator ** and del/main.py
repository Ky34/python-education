# Распаковка словарей

button = {
    'width': 200,
    'text': 'Buy'
}

red_button = {
    **button,
    'color': 'red'
}

print(red_button)
print(button)


# Оъединение словарей

button_ifo = {
    'text': 'Buy'
}

button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300
}

# для объединения словарей используеться прямая черта |
# в случае, если в словарях есть одинаковые ключи,
# порядок следования операндов важен
button = button_ifo | button_style

print(button)


button_default = {
    'text': 'Ok',
    'color': 'black',
    'width': 0,
    'height': 0
}

button = button_default | button_style
print(button)

button = button_default | button_style | button_ifo
print(button)


# Инструкция del

my_list = [1, 2]

# print(del my_list[0])  # SyntaxError: invalid syntax
del my_list[0]
my_list.__delitem__(0)

print(my_list)  # []
