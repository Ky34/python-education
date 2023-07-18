
def hello(name):
    print('Hello there,', name)
    print('Hi there,', name)


hello('Valera')
hello('Masha')


def sum_nums(a, b):
    sum = a + b
    # при отсутствии ключевого слова return любая функция возвращает None
    return sum
    # этот код не будет выполнен, так как функия заканчивает выполнения после слова return
    print('line is not executed')


first_sum = sum_nums(10, 5)
print(first_sum)

print(print('Alesha'))

print(sum_nums(50.5, 20))

print(sum_nums(sum_nums(10, 5), 30))
