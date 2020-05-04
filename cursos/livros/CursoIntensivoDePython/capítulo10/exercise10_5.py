# -*- coding: utf-8 -*-
"""
Chapter 10 - Arquivo e Excessões (Ex. 10.10 - page 278)
Book: Curso Intensivo de Python
Date: 24Apr2020
Obs.: 
"""

filename = "text_files/pi_million_digits.txt"

birthday = input("Enter the date of your birthday in a format mmddyy: ")

if birthday in filename:
    print("Your birthday is in Pi number")
else:
    print ("Your birthday is not in Pi number")