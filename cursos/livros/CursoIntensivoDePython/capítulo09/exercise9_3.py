# -*- coding: utf-8 -*-
"""
Chapter 9 - Classes (Ex. 9.3 - page 226)
Book: Curso Intensivo de Python
Date: 20Apr2020
"""

class User():
    def __init__(self,first_name,last_name,birth_year,marital_status):
        self.first_name = first_name.title()
        self.last_name = last_name.upper()
        self.birth_year = birth_year
        self.marital_status = marital_status.title()
        
    def describe_user(self):
        print ("\nThe user's name is " + self.first_name + " " + self.last_name + ".")
        print (self.first_name + "'s mariatal status is " + self.marital_status + ".")
        print (self.first_name + " was born in " + str(self.birth_year) + ".")
        
    def greet_user(self):
        print ("\nThanks " + self.first_name + " for learning Python programming!")
        
user_01 = User("Cassio","mendonca",1977,"married")
user_02 = User("Daniela","mendonca",1980,"married")

user_01.describe_user()
user_02.describe_user()
user_01.greet_user()
user_02.greet_user()

