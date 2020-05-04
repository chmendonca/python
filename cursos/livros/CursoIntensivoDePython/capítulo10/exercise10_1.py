# -*- coding: utf-8 -*-
"""
Chapter 9 - Classes (Ex. 10.1 - page 263)
Book: Curso Intensivo de Python
Date: 24Apr2020
Obs.: 
"""

filename = 'text_files/learning_python.txt'

with open(filename) as my_file:
    phrases = my_file.read()

p1 = 0  
while p1 <= 2:
    print(phrases)
    p1 += 1
    
print (30*"-")
with open (filename) as my_file:
    for line in my_file:
        print (line.rstrip())
        
print (30*"=")
with open(filename) as my_file:
    phrases = my_file.readlines()
    
for line in phrases:
    print (line.rstrip())