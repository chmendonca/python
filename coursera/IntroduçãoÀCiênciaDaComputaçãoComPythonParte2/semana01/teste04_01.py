def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)

    for i in range(num_colunas):
        for j in range(num_linhas):
            matriz[j][i] = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))

    return matriz

print('\nmatriz 1\n')
print(cria_matriz(2,3))

'''
def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        coluna = []
        for j in range(num_colunas):
            coluna.append(0)
        matriz.append(coluna)

    for i in range(num_linhas):
        for j in range(num_colunas):
            matriz[j][i] = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: "))

    return matriz

print('\nmatriz 2\n')
cria_matriz(2,3)
'''
def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_colunas):
        coluna = []
        for j in range(num_linhas):
            valor = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))
            coluna.append(valor)
        matriz.append(coluna)
    return matriz

print('\nmatriz 3\n')
print(cria_matriz(2,3))

def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_colunas):
        linha = []
        for j in range(num_linhas):
            valor = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

print('\nmatriz 4\n')
print(cria_matriz(2,3))