# сокращенный for in используется для создания
# новых последовательностей на основании существующей

all_nums = [-3, 1, 0, -20, 5]

# с использованием обычного цикала
absolute_nums = []
for num in all_nums:
    absolute_nums.append(abs(num))

print(absolute_nums)

# при помощи сокращенного цикла
absolute_nums = [abs(num) for num in all_nums]
print(absolute_nums)


all_nums = [-3, 1, 0, 10, -20, 5]

# c использованием обычного цикла

positive_nums = []
for num in all_nums:
    if num > 0:
        positive_nums.append(num)

print(positive_nums)

# с помощью сокращенного цикла

positive_nums = [num for num in all_nums if num > 0]

print(positive_nums)
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++==')


# examples:
# Sets

my_set = {1, 10, 15}

# c использованием обычного цикла

new_set = set()
for val in my_set:
    new_set.add(val * val)

print(new_set)
print(my_set)

# c помощью сокращенного цикла

new_set = {val * val for val in my_set}
print(new_set)


# Dicts

my_scores = {
    'a': 10,
    'b': 7,
    'c': 14
}

my_scores_list = [10, 7, 14]

# с использованием обычного цикла

scores = {}

for key, value in my_scores.items():
    scores[key] = value * 10

print(scores)
print(my_scores)

# c помощью сокращенного цикла

scores = {key: value * 10 for key, value in my_scores.items()}

# из словаря создаем множество из значений
scores_one = {value * 10 for key, value in my_scores.items()}

# функция enumerate возвращает
# последовательность кортежей из пар (индекс, элемент)
# c помощью сокращенного цикла создаем словарь где ключ - это индекс
# элемента из последовательности а значение - сам элемент
scores_two = {index: elem for index, elem in enumerate(my_scores_list)}

print(scores)
print(scores_one)
print(scores_two)
