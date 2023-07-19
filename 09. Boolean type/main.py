# Boolean types

db_is_available = False
print(db_is_available)
print(type(db_is_available))

db_is_available = True

print(db_is_available)
print('=====================================')
print(bool(10))
print(bool('abc'))
print(bool([]))
print(bool([1, 2]))
print(bool(None))
print(bool({'abc': 1, 'cde': 2}))
print(bool({}))
print('-------------------------------------')
print(100 > 10)
#  при сравнении строк идет посимвольное сравнение
print('Long string' > 'Short')  # False
print('Long string' > 'Long')  # True
print([] == [])
print({'a': 3} == {'a': 5})
