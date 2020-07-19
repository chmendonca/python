# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:22:00 2020

@author: Cassio
"""

def remove_repetidos(lista):
    lista = sorted(list(set(lista)))
    print(lista)
    return lista
    
lista = [3,4,1,1,4]
remove_repetidos(lista)