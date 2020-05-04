# -*- coding: utf-8 -*-
"""
Chapter 10 - Arquivos e Excesso~es (Exemplo - page 280 until )
Book: Curso Intensivo de Python
Date: 24Apr2020
Obs.: 
"""

import json

filename = 'numbers.json'

with open(filename) as fj:
    numbers = json.load(fj)
    
print (numbers)