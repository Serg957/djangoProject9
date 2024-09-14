immutable_var = 1, 2.5, 'string', True
print(immutable_var)
# immutable_var[0] = 4
# print(immutable_var)
error = 'Кортеж хранит ссылку на список , а не сам список.'
print(error)

mitable_list = ['pen', 'book', 'pencil', 'notebook']
print(mitable_list)
mitable_list[0] = 'mouse'
mitable_list[2] = True
print(mitable_list)