my_range = range(5)

print(my_range)
print(type(my_range))
print(my_range[0])

for n in range(12, 25, 5):
    print(n)

print(list(range(12, 25, 5)))
print(tuple(range(12, 25, 5)))
print(set(range(12, 25, 5)))

my_range = range(10, 30, 3)
print(my_range.start)
print(my_range.stop)
print(my_range.step)
print(my_range.index(13))
# print(my_range.index(12))  # ValueError: 12 is not in range
# .count() передает 1 если элемент есть в диапозоно и 0 если нет
print(my_range.count(11))
print(my_range.count(10))

new_range = range(10, 100, 5)
new_list = []

for i in new_range:
    new_list.append(i)

print(new_list)
