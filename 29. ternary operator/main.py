# У тернароного оператора 3 операнда
# конструкция с тернарным оператором является выражением


my_number = 21.5

print("is int") if type(my_number) is int else print("is not int")

# send_img(img) if img.get['is_processed'] else process_and_send_img(img)

product_qty = 10

print("in stock" if product_qty > 0 else "out of stock")

temp = +24

weather = "hot" if temp > 18 else "cold"
print(weather)


# practice

my_img = ('1920', '1080')

print(f"{my_img[0]}x{my_img[1]}") if len(
    my_img) == 2 else print("incorrect img formating")


if len(my_img) == 2:
    print(f"{my_img[0]}x{my_img[1]}")
else:
    print("incorrect img formating")


def how_long_string(string):
    return print("string is long") if len(string) > 79 else print("string is short")


my_string = 'assdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasd'
my_string_one = 'asdasdasdasdasdasdasdasdasdasdasdasdasdasdasd'

how_long_string(my_string)
how_long_string(my_string_one)
