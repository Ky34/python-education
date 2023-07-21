# Функции

def sum(a, b):
    c = a + b
    print(c)


a = 5
b = 3

sum(a, b)

print(type(sum))  # <class 'function'>
# функция возвращает None если нет ключевого слова return


# самая короткая функция в Python


def my_fn():
    pass  # ключевое слово, которое используется для заполнения пустого тела функции\цикла


print(my_fn())  # None


# Передача изменяемых объектов в функцию
# при передаче изменяемых объектов,
# функция может изменять внешние переменные

def increase_person_age(person):
    print(id(person))
    person['age'] += 1
    return person


person_one = {
    'name': 'Bob',
    'age': 21
}

print(id(person_one))

increase_person_age(person_one)
print(person_one['age'])

# внутри функции не рекомендуется изменять внешние объекты

# чтобы избежать изменения внешнего объекта при использовании функции
# можно созать поверхностную или глубокую копию объекта


def increased_person_age(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy


person_one = {
    'name': 'Bob',
    'age': 21
}

new_person = increased_person_age(person_one)
print(new_person['age'])  # 22
print(person_one['age'])  # 21
