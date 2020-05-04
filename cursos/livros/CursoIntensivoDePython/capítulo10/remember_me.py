# -*- coding: utf-8 -*-
"""
Chapter 10 - Arquivos e Excesso~es (Exemplo - page 280 until )
Book: Curso Intensivo de Python
Date: 24Apr2020
Obs.: 
"""

import json

filename = 'username.json'
user_list = []
with open(filename,"w") as f:
    f.write("")
    
while True:
    user = input("What's your name: ")
    if user == "quit":
        break
    user_list.append(user)
    print (user + ", I will remember you when you come back!")
    
with open(filename,"a") as fj:
    json.dump(user_list,fj)

with open(filename) as fj:
    user = json.load(fj)
    for each in user:
        print (each + " already logged in anytime!")