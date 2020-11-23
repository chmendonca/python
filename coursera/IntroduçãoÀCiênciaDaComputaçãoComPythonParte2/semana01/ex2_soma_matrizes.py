def tamanho_matriz(m):
    number_lines = len(m)
    size_check = []
    for line in m:
        size_check.append(len(line))
    if all(l == len(line) for l in size_check):
        return str(number_lines) + "X" + str(len(line))
    else:
        return "Invalid Matrix"

def soma_matrizes(m1,m2):
    if tamanho_matriz(m1) == tamanho_matriz(m2):
        matrix = []
        for line in range(len(m1)):
            new_line = []
            m1_line = m1[line]
            m2_line = m2[line]
            for column in range(len(m1[line])):
                new_line.append(m1_line[column] + m2_line[column])
            matrix.append(new_line)
        return matrix
    else:
        return False

'''
print('\nmatriz 1\n')
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(soma_matrizes(m1, m2)) #=> [[3, 5, 7], [9, 11, 13]] 

print('\nmatriz 2\n')
m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(soma_matrizes(m1, m2)) #=> False
'''