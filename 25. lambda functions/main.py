# Функция

def mult(a, b):
    return a * b


print(mult(10, 5))

# Лямбда функция

lambda a, b: a * b


# пример использования лямбда функции

def greeting(greet):
    def info(name):
        return f"{greet}, {name}"
    return info

# та же функция с использованием лямбда функции


def greeting(greet):
    return lambda name: f"{greet}, {name}"


# возвращаем результат функции greeting() и присваиваем его переменной
morning_greeting = greeting("Good Morning")
# теперь переменная morning_greeting тоже является функцией

print(morning_greeting('Alesha'))

evening_greeting = greeting("Good Evening")

print(evening_greeting("Valera"))
