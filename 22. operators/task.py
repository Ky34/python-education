# 1.

my_set = {10, 15, 20, 40}
other_set = {10, 15, 20, 40}

print(my_set == other_set)  # True - одинаковые значения в множествах
print(my_set.__eq__(other_set))

print(id(my_set) == id(other_set))  # False - но объекты разные

print(my_set is other_set)  # при использовании is сравниваются id

print(10 in my_set)  # True
print(17 in my_set)  # False
print(11 not in my_set)  # True
