my_dict = {'Sergey': 1987, 'Olga': 1990, 'Ivan': 2010}
print(my_dict)
print(my_dict['Olga'])
print(my_dict.get('Sasha', 'Такого имени нет.'))
my_dict.update({'Egor': 1998, 'Polina': 2001})
print(my_dict)
a = my_dict.pop('Polina')
print(a)
print(my_dict)

my_set = {1, 2, 3, 3, 2, 1, 1.25, (1, 2, 3),
          'string', (1, 2, 3), 'string', 1.25}
print(my_set)
print(my_set.add(5))

print(my_set.add('solution'))
print(my_set)
print(my_set.discard('solution'))
print(my_set)
