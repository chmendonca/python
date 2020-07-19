# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 12:48:23 2020

@author: Cassio
"""
def imprime_retangulo_cheio(l,a):
    pl = 0
    pa = 0
    while pa < a:
        while pl < l:
            print("#",end="")
            pl+=1
        print()
        pl = 0
        pa+=1
            
def main():
    """Imprime um retângulo de hashtags de acordo com os numeros entrados"""
    enterMsg1 = "digite a largura: "
    enterMsg2 = "digite a altura: "
    while True:
         try:
            l = int(input(enterMsg1))
            a = int(input(enterMsg2))
            if l > 0 and a > 0:
                break
            else:
                print("\nAtenção: 'n' e 'm' devem ser inteiros maiores que 0")
                continue
         except:
            print("\nPor favor, insira somente números inteiros maiores que 0!")
    
    imprime_retangulo_cheio(l,a)

main()