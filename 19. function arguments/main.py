# функция может принимать любое колличество аргументов,
# если их объеденить в кортеж
# порядок передачи аргументов в функцию важен

from datetime import date


def sum_nums(*args):  # синтаксис
    print(args)  # (2, 3, 7) - кортеж
    print(type(args))  # <class 'tuple'>
    print(args[0])  # 2
    return sum(args)


print(sum_nums(2, 3, 7))  # 12
print('---------------------------------------------------')


# аргументы с ключевыми словами
# в аргументах с ключевыми словами порядок не важен


def get_posts_info(name, posts_qty):
    info = f'{name} wrote {posts_qty} posts'
    return info


# порядок не важен
info = get_posts_info(name='Alesha', posts_qty=25)  # Alesha wrote 25 posts
info = get_posts_info(posts_qty=25, name='Alesha')  # Alesha wrote 25 posts

print(info)


# объединение аргументов в словарь

def get_posts_information(**person):  # синтаксис
    print(person)  # {'name': 'Alesha', 'posts_qty': 25}
    print(type(person))  # <class 'dict'>
    # такой синтаксис используется, чтобы не было длинной строки
    info = (
        # если не ставить запятую, Pyton объеденит 2 строки
        f"{person['name']} wrote "  # <- тут
        f"{person['posts_qty']} posts"
    )
    return info


info = get_posts_information(name='Alesha', posts_qty=25)
print(info)


# Параметры функции по умолчанию

def mult_by_factor(value, multiplier=1):  # <- значение по умолчанию
    return value * multiplier


print(mult_by_factor(10, 2))  # 10
print(mult_by_factor(5))  # 5


print('------------------------------------------------------')
# from datetime import date


def get_weekday():
    return date.today().strftime('%A')

# значением по умолчанию для параметра
# может быть и результат вызова функции


def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['created_on_weekday'] = weekday
    return post_copy


initial_post = {
    'id': 243,
    'author': 'Alesha'
}

post_with_weekday = create_new_post(initial_post)
print(post_with_weekday)
print(initial_post)
