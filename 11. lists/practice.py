# Lists practice

my_nums = [10, 50, 0, 5, 5, 100]
print(dir(my_nums))  # список методов

res = my_nums.count(5)  # колличество элементов 5 в списке
print(res)  # 2

my_nums.append(25)
print(my_nums)

# вставляет элемент -5 перед элементов с индексом [2] в списке
my_nums.insert(2, -5)
print(my_nums)

my_nums.clear()  # очищает список
print(my_nums)

my_nums = [10, 50, 0, 5, 5, 100]
my_nums.extend('abc')  # [10, 50, 0, 5, 5, 100, 'a', 'b', 'c']
# так же методом .extend() можно добавить в текущий список другой список
print(my_nums)

other_nums = my_nums.copy()

my_nums.append(3)
other_nums.clear()

print(id(my_nums))
print(id(other_nums))
print(my_nums, other_nums)
print(len(my_nums))
