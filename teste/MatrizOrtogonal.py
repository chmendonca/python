import pandas as pd

from Dados import Dados as dds

class MatrizOrtogonal():
    def __init__(self):
        super().__init__()

    def filtrandoMatrizOrtogonalMaiorIgualNumeroVariaveis(self,n,lmo):
        """Esta função exclui todas as possibilidades de matrizes em que o maior
           número de variáveis da matriz ortogonal é menor que o maior número de
           de variáveis testedas"""
        print(lmo)
        #print(lmo['maior numero variaveis'])
        #print(n.iloc[0,0])
        lmo_maior_igual_variaveis = lmo['maior numero variaveis'] >= n.iloc[0,0]
        lmo = lmo[lmo_maior_igual_variaveis]
        print(lmo)
        
        return lmo

    def filtrandoMatrizOrtogonalNumeroTotalColunas(self,n,lmo):
        """Esta função exclui todas as possibilidades de matrizes em que o número
           total de colunas da matriz ortogonal é menor que o número de colunas
           da maior variável e é do tipo 1"""
        lmo_maior_igual_colunas = -((lmo['numero colunas maior variavel'] < self.n['numero_colunas_mesmo_valor'].sum()) & (lmo['tipo'] == "t1"))
        lmo = lmo[lmo_maior_igual_colunas]
        print(lmo)

        return lmo

    def filtrandoMatrizOrtogonalMenorNumeroVariaveis(self,n,lmo):
        pass
