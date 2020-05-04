# -*- coding: utf-8 -*-
"""
Chapter 10 - Arquivo e Excessões (Ex. 10.10 - page 278)
Book: Curso Intensivo de Python
Date: 24Apr2020
Obs.: 
"""

filename = "text_files/pi_million_digits.txt"

birthday = input("Enter the date of your birthday in a format mmddyy: ")

with open(filename) as f:
    pi_number = f.readlines()
    #print(pi_number)
    pi_string = ""
    for line in pi_number:
        pi_string += line.strip()
#    print(pi_string)
#    print(len(pi_string))
        
    if birthday in pi_string:
        print("Your birthday is in Pi number")
    else:
        print ("Your birthday is not in Pi number")
        
    print(pi_string.count(birthday))
    
    