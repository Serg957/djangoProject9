def all_variants(text):
    len_ = len(text)
    for x in range(len_): # сколько букв добавляем в комбинацию.
        for i in range(len_): # позиция перебора
            yield text[i:i+x+1]
        len_ = len_ - 1

a = all_variants("abc")
for i in a:
    print(i)
print()

