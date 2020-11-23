def dimensoes(minha_matriz):
    number_lines = len(minha_matriz)
    number_columns = len(minha_matriz[0])
    print(str(number_lines) + "X" + str(number_columns))
    '''
    size_check = []
    for line in minha_matriz:
        size_check.append(len(line))
    if all(l == len(line) for l in size_check):
        return str(number_lines) + "X" + str(len(line))
    else:
        return "Invalid Matrix"
    '''

'''
minha_matriz = [[1, 2, 7, 1], [3, 4, 8, 1], [1, 2, 3, 1]]
print(dimensoes(minha_matriz))

minha_matriz = [[1],[2],[3]]
print(dimensoes(minha_matriz))

minha_matriz = [[1,2,3],[4,5,6]]
print(dimensoes(minha_matriz))

minha_matriz = [[1,2,3],[4,5,6,5]]
print(dimensoes(minha_matriz))
'''