def print_params(a=1, b='строка', c=True):
    print(a, b, c)


valies_list = [7, 'проверка', 3.25]

valies_dict = {'a': 5, 'b': 'зачет', 'c': 5.5}

valies_list_2 = [57.70, 'cтрока']

print_params()
print_params(a=2, b=25)
print_params(c=[1, 2, 3])
print_params(a='Верно', b='или', c='нет')
print_params(*valies_list)
print_params(**valies_dict)
print_params(*valies_list_2, 42)
