def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


a = get_matrix(2, 3, 12)
b = get_matrix(3, 4, 17)
c = get_matrix(1, 3, 2)
print(a)
print(b)
print(c)
