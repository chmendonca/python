import random

class ListaAleatoria:
    def lista_aleatoria(self, n):
        #lista = [0 for x in range(n)] #cria uma lista de 0 (zeros) de comprimento n
        max_value = 1000
        lista = [random.randrange(max_value)for x in range(n)]
        return lista

    def lista_quase_ordenada(self,n):
        lista = [x for x in range(n)] #cria uma lista ordenada de tamanho n
        lista[n//10] = -500 #inserir o valor de -500 no começo da lista
        return lista

    def cria_duas_listas(self,n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:] #clona a lista1 e portanto são diferentes
        return lista1, lista2

    def cria_tres_listas_aleatorias(self,n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:] #clona a lista1 e portanto são diferentes
        lista3 = lista1[:] #clona a lista1 e portanto são diferentes
        return lista1, lista2, lista3

    def cria_tres_listas_quase_ordenadas(self,n):
        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:] #clona a lista1 e portanto são diferentes
        lista3 = lista1[:] #clona a lista1 e portanto são diferentes
        return lista1, lista2, lista3
