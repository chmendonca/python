import os

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
        lmo = dds.abrirArquivoCsv(self,os.path.join(os.getcwd(),"lista_matrizes_ortogonais.csv"))
        print(lmo)

if __name__ == "__main__":
    m = main()
    m.abrirArquivo()
    m.calcularMatrizTeste()
    m.calcularMatrizOrtogonal()
    