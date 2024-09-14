def f1(number):
    return 10/number

# def f2():
#     print('Какой хороший день')
#     result_f1 = f1(0)
#     return result_f1
# def f2():
#     print('Какой хороший день')
#     summ = 0
#     for i in range(-2,2):
#         summ+= f1(i)
#         print(summ)
#     return summ
def f2():
    summ = 0
    for i in range(-2, 2, 1):
        try:
            summ += f1(i)
            print(summ)
        except ZeroDivisionError as exc:
            print(f' внутри f1 что-то пошло не так: {exc}, но программа жива, мы молодцы ')
    return summ / 0


try:
    total = f2()
    print(f' Вот ваш результат функции: {total}')
     # print(total)
except ZeroDivisionError as exc:
    print(f' вот что пошло не так - {exc}, но мы устояли')
