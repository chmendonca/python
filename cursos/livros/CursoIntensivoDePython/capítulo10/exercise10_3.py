# -*- coding: utf-8 -*-
"""
Chapter 9 - Classes (Ex. 10.3 - page 266)
Book: Curso Intensivo de Python
Date: 24Apr2020
Obs.: 
"""

filename = "text_files/guest.txt"

user=input("What's your name: ")
with open(filename,'a') as user_file:
    user_file.write(user + "\n")