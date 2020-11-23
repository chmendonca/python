def multiplica_matrizes(A,B):
    #B = inverting_matrix(B)
    multiplicated_matrix = []
    for rowA in range(len(A)):
        multiplicated_row = []
        for colB in range(len(B[0])):
            multiplicated_value = 0
            for pos_row_A in range(len(A[0])):
                multiplicated_value += (A[rowA][pos_row_A]*B[pos_row_A][colB])
            multiplicated_row.append(multiplicated_value)
        multiplicated_matrix.append(multiplicated_row)
    return multiplicated_matrix
        
print('\nmatriz 1\n')
A = [[1, 2, 3], [4, 5, 6]]
B = [[1, 2],[3, 4],[5, 6]]
print(multiplica_matrizes(A,B))