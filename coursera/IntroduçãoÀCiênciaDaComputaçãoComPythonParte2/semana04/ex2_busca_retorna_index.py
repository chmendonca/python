# class Busca:
#     def busca(self,lista,elemento):
#         for item in lista:
#             print(item)
#             if item == elemento:
#                 return lista.index(item)
#         else:
#             return False

# # b = Busca()
# # print(b.busca([1,2,3],2))

'''
Neste exercício, você não deve utilizar o método index
'''
def busca(lista,elemento):
    for pos in range(len(lista)):
        if lista[pos] == elemento:
            return pos
    else:
        return False

# print(busca([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], 30))