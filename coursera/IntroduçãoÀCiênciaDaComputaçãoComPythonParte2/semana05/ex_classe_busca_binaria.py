class Buscador:
    def busca_sequencial(self,lista,x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1

    def busca_binaria(self,lista,x):
        '''This algorithm is used only in ordered lists'''
        primeiro = 0
        ultimo = len(lista) - 1
        while primeiro <= ultimo:
            meio = (primeiro + ultimo )//2 #just in case of the list with odd numbers
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        return -1

lista = [0,1,2,3,4,5,6]
b = Buscador()
print(b.busca_binaria(lista,3))
print(b.busca_binaria(lista,0))
print(b.busca_binaria(lista,-2))