# import io
# from pprint import  pprint
#
# name = 'sample2.txt'
# with open(name, encoding='utf-8') as file:
#     for line in file:
#         for char in line:
#             print(char, end='')
#     print(file.tell())
# print('Привет, '+ 'мир!')
# print('Меня зовут %(name)s, мне %(year)s' % {'name':'Денис', 'year' :14})
# print("Я учусь в {title}{postfix} {title}" .format(title='Урбан',postfix='-university'))
# print(f'{"Urban" * 2} это лучший университет!')
#
#
import os
from os import mkdir

print('Текущая директория:', os.getcwd())
if os.path.exists('second'):
    os.chdir('second')
else:
    os,mkdir()
    os.chdir()
print('Текущая директория:', os.getcwd())
print(os.listdir())
for i in os.walk('.'):
# os.makedirs(r'third\fourth')
    print(i)
os.chdir(r'D:\PycharmProjectsmy\lesson\module_7_0.py' )
print('Текущая директория:', os.getcwd())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(dirs)
print(file)