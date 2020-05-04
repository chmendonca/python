# -*- coding: utf-8 -*-
"""
Chapter 10 - Arquivos e Excesso~es (Exemplo - page 264)
Book: Curso Intensivo de Python
Date: 24Apr2020
Obs.: 
"""

filename = 'text_files/programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming")
    
with open(filename,'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
    
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    
with open(filename, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser")