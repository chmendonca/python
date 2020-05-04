# -*- coding: utf-8 -*-
"""
Chapter 10 - Arquivos e Excesso~es (Exemplo - page 279 until )
Book: Curso Intensivo de Python
Date: 24Apr2020
Obs.: 
"""

import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'

with open(filename,"w") as fj:
    json.dump(numbers,fj)