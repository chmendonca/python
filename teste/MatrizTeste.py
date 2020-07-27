import pandas as pd

class MatrizTeste():
    def __init__(self):
        super().__init__()
    
    def combinacoesTestes(self,df):
        combinacoes = 1
        for variavel in df.columns:
            combinacoes *= df[variavel].count()
        print("\ncombinacoes: ",combinacoes)

        return combinacoes

    def numeroValores(self,df):
        matriz_valores_colunas = (df.count().value_counts()).sort_index(ascending = False)
        matriz_valores_colunas = matriz_valores_colunas.to_frame()
        matriz_valores_colunas = matriz_valores_colunas.reset_index()
        matriz_valores_colunas.columns = ["numero_valores_por_coluna","numero_colunas_mesmo_valor"]
        print("\nmatriz de valores das colunas:")
        print(matriz_valores_colunas)

        return matriz_valores_colunas

    def matrizNaoOrtogonal(self,c,n):
        dentro_parenteses = ""
        for index in range(n.shape[0]):
            dentro_parenteses += str(n.iloc[index,0]) + "**" + str(n.iloc[index,1]) + " "
        mno = "L" + str(c) + "(" + dentro_parenteses.rstrip() + ")"
        print("\nmatriz nao ortogonal:")
        print(mno)