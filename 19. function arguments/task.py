# Task 1

def merge_list_to_dict(list_one, list_two):
    return dict(zip(list_one, list_two))


res_one = merge_list_to_dict(list_one=['a', 'b', 'c'], list_two=[10, True, []])
print(res_one)

res_two = merge_list_to_dict(['a', 'b', 'c'], list_two=[1, 2, 3])
print(res_two)


# Task 2

def update_car_info(**car):
    car['is_available'] = True
    return car


car_one = update_car_info(car='Toyota', price=9200)
print(car_one)
