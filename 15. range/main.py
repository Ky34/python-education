# Range

my_range = range(7)

print(type(my_range))  # <class 'range'>
print(my_range)  # range(0, 7) от 0 включительно до 7 не включительно
print(list(my_range))  # [0, 1, 2, 3, 4, 5, 6]

# при создании диапозона можно указать начальное значение,
# конечное, а так же шаг

my_range = range(10, 20, 3)  # 3 - шаг для диапозона

print(my_range)  # range(10, 20, 3)
print(list(my_range))  # [10, 13, 16, 19]

print(my_range[0])  # 10
print(my_range[1])  # 13
print(my_range[2])  # 16
print(my_range[3])  # 19
# print(my_range[4])  # IndexError: range object index out of range

for n in my_range:
    print(n)
