def bubble_sort(lista):
    fim = len(lista)
    # print('fim = %s' %fim)
    for i in range(fim - 1, 0, -1):
        # print('i = %s' %i)
        trocou = False
        for j in range(i):
            # print('j = %s' %j)
            if lista[j] > lista[j+1]:
                # print('lista[j] = %s' %lista[j])
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
                print(lista)
            # print('lista = %s' %lista)
        if not trocou:
            return lista
    return lista

# lista = [5, 1, 4, 2]
# bubble_sort(lista)