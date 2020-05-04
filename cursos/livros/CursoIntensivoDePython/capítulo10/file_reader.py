# -*- coding: utf-8 -*-
"""
Chapter 10 - Arquivos e Excesso~es (Exemplo - page 255 to 260)
Book: Curso Intensivo de Python
Date: 24Apr2020
Obs.: 
"""

with open( 'pi_digits.txt') as file_object:
    contents = file_object.read()
    print (contents.rstrip())
    
with open('text_files/pi_digits_2.txt') as file_object:
    contents = file_object.read()
    print (contents)
    
with open('text_files/pi_digits_2.txt') as file_object:
    for line in file_object:
        message = "read line: " + line
        print (message.rstrip())
        
print (30*"-")

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    print ("lines: ",lines)

for line in lines:
    print("line: ",line.rstrip())