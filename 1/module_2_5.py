def get_matrix(n, m, value):
    matrix_out = []
    for i in range(n):
        matrix_in = []
        for k in range(m):
            matrix_in.append(value)
        matrix_out.append(matrix_in)
    return matrix_out

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)