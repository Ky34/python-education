# call-back функция вызывается в теле другой функции

def other_fn():
    pass


def fn_with_callback(callback_fn):
    callback_fn()


fn_with_callback(other_fn)

# 3


def print_number_info(num):
    if (num % 2) == 0:
        print('Вы ввели парное число')
    else:
        print('Вы ввели непарное число')


def print_square_num(num):
    print('Квадрат числа равен ', num * num)


def process_number(num, callback_fn):
    callback_fn(num)


entered_num = int(input('Введите любое целое число: '))

process_number(entered_num, print_number_info)
process_number(entered_num, print_square_num)


############################################################

def send_data(data):
    pass


def process_data(input_data, send_data_fn):
    updated_data = input_data.copy()
    send_data_fn(updated_data)


process_data({'name': 'Alesha'}, send_data)
