# -*- coding: utf-8 -*-
"""
Chapter 10 - Arquivo e Excessões (Ex. 10.4 - page 267)
Book: Curso Intensivo de Python
Date: 24Apr2020
Obs.: 
"""

filename = "text_files/guest_book.txt"

user = ""

while user != "quit":
    user=input("Type your name: ")
    if user != "quit":
        with open(filename,'a') as user_book:
            print ("Thanks for comming " + user)
            user_book.write(user + "\n")
    else:
        print ("Closing file")