# -*- coding: utf-8 -*-
"""
Chapter 10 - Arquivos e Excesso~es (Exemplo - page 260)
Book: Curso Intensivo de Python
Date: 24Apr2020
Obs.: 
"""
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string1 = ""
pi_string2 = ""
pi_string3 = ""

for line in lines:
    pi_string1 += line.rstrip()
    pi_string2 += line
    pi_string3 += line.strip()
    
print (pi_string1)
print (len(pi_string1))
print (pi_string2)
print (len(pi_string2))
print (pi_string3)
print (len(pi_string3))
print (30*"-")
print (pi_string3[:6])
print (len(pi_string3))

print (30*"*")
filename = 'text_files/pi_million_digits.txt'

pi_string_m = ""

with open(filename) as file_object:
    lines = file_object.readlines()
    #print (lines)
    
for line in lines:
    pi_string_m += line.strip()
    
print (pi_string_m[:52])
print (len(pi_string_m))

print (30*"!")

with open(filename) as file_object:
    lines = file_object.read()
    
birthday = input("Type your birth date in a format mmddyy: ")
if birthday in lines:
    print ("Your birthday is in Pi number")
else:
    print ("No, your birthday isn't in Pi number")


