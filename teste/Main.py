import os
import pathlib

from Dados import Dados as dds
from MatrizTeste import MatrizTeste as mt
from MatrizOrtogonal import MatrizOrtogonal as mo

class main():
    def __init__(self):
        super().__init__()
    
    def abrirArquivo(self):
        dados = dds.importarDados(self)
        self.df = dds.abrirArquivoCsv(self,dados)

    def calcularMatrizTeste(self):
        c =  mt.combinacoesTestes(self,self.df)
        self.n = mt.numeroValores(self,self.df)
        mt.matrizNaoOrtogonal(self,c,self.n)

    
    def calcularMatrizOrtogonal(self):
        lmo = dds.abrirArquivoCsv(self,os.path.join(os.path.dirname(os.path.abspath(__file__)),"mtz_ortogonal\\lista_matrizes_ortogonais.csv"))
        lmo = mo.filtrandoMatrizOrtogonalMaiorIgualNumeroVariaveis(self,self.n,lmo)
        lmo = mo.filtrandoMatrizOrtogonalNumeroTotalColunas(self,self.n,lmo)

        #numero_colunas_menor_igual_menor_numero_variaveis = self.n

        tipo = lmo['tipo'] == 't2'
        lmo = lmo[tipo]
        print(lmo['tipo'].count())
        contagem_t2 = lmo['tipo'].count()
        for t2 in range(contagem_t2):
            print(t2)
        



if __name__ == "__main__":
    m = main()
    m.abrirArquivo()
    m.calcularMatrizTeste()
    m.calcularMatrizOrtogonal()
    