my_name = 'Alesha'
my_hobby = 'running'
time = 8
my_list = [1, 3, 5]

info = my_name + ' likes ' + my_hobby + ' at ' + str(time) + " o'clock"
# в f строке можно использовать значения других типов без явной конвертации
new_info = f"{my_name} likes {my_hobby} at {time} o'clock"

next_string = f"hello {my_name}. now {time} o'clock and its time to {my_hobby}, but tell me, is it you favorite numbers {my_list}???"

print(info)
print(new_info.title())
print(next_string)
