import time
from ex_classe_lista_aleatoria import ListaAleatoria

class Ordenador:
    def selecao_direta(self,lista):
        fim = len(lista)
        for i in range(fim - 1):
            #Inicialmente o menor elementa já visto é o i-ésimo
            posicao_do_minimo = i
            for j in range(i + 1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            #Coloca o menor elemento encontrado no início da sub-lista
            #Para isso, troca de lugar os elementos nas posições i e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
        return lista

    def bolha(self, lista):
        fim = len(lista)
        # print('fim = %s' %fim)
        for i in range(fim - 1, 0, -1):
            # print('i = %s' %i)
            for j in range(i):
                # print('j = %s' %j)
                if lista[j] > lista[j+1]:
                    # print('lista[j] = %s' %lista[j])
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                # print('lista = %s' %lista)
        return lista

    def bolha_curta(self, lista):
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
                # print('lista = %s' %lista)
            if not trocou:
                return lista
        return lista


o = Ordenador()
l = ListaAleatoria()


print('--- Lista aleatória ---')
#lista1, lista2 = l.cria_duas_listas(5000)
lista1, lista2, lista3 = l.cria_tres_listas_aleatorias(5000)
#print(lista1)
#print(lista2)

antes = time.time()
#print(o.selecao_direta(lista1))
o.selecao_direta(lista1)
depois = time.time()
print("seleção direta = ", depois - antes)

antes = time.time()
#print(o.bolha(lista2))
o.bolha(lista2)
depois = time.time()
print("bolha = ", depois - antes)

antes = time.time()
#print(o.bolha(lista2))
o.bolha_curta(lista3)
depois = time.time()
print("bolha curta = ", depois - antes)
#lista1, lista2 = l.cria_duas_listas(5000)

print('--- Lista quase ordenada ---')
lista1, lista2, lista3 = l.cria_tres_listas_quase_ordenadas(5000)
#print(lista1)
#print(lista2)

antes = time.time()
#print(o.selecao_direta(lista1))
o.selecao_direta(lista1)
depois = time.time()
print("seleção direta = ", depois - antes)

antes = time.time()
#print(o.bolha(lista2))
o.bolha(lista2)
depois = time.time()
print("bolha = ", depois - antes)

antes = time.time()
#print(o.bolha(lista2))
o.bolha_curta(lista3)
depois = time.time()
print("bolha curta = ", depois - antes)