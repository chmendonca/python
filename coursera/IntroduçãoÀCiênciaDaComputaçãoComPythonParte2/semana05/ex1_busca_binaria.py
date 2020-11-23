def busca(lista,elemento):
    first = 0
    last = len(lista) - 1
    while first <= last:
        middle = (first + last) // 2
        print(middle)
        if lista[middle] == elemento:
            return middle
        else:
            if elemento <= lista[middle]:
                last = middle - 1
            else:
                first = middle + 1
    
    #print(middle)
    return False

# lista1 = ['a','e','i']
# lista2 = [1,2,3,4,5]
# lista3 = [1,2,3,4,5,6]
# print(busca(lista1,'e'))
# print(busca(lista2,6))
# print(busca(lista3,4))

