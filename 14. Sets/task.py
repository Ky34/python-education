# 1.

my_set = {1, 2, 3, 4, 5}
print(type(my_set))

# 2.

my_set.add(100)
print(my_set)

# 3.

other_set = {1, 2, 10, 8, 7}

# 4.

new_set = my_set.intersection(other_set)
print(new_set)

# 5.

new_list = list(new_set)
print(new_list)

other_set.remove(8)
print(other_set)

dif = my_set.symmetric_difference(other_set)
print(dif)
