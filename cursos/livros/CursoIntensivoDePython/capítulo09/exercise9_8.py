# -*- coding: utf-8 -*-
"""
Chapter 9 - Classes (Ex. 9.7 - page 241)
Book: Curso Intensivo de Python
Date: 20Apr2020
Obs.: This exercise uses the exercise 9.5 as basis
"""

#page 232
class User():
    def __init__(self,first_name,last_name,birth_year,marital_status,login_attempts):
        self.first_name = first_name.title()
        self.last_name = last_name.upper()
        self.birth_year = birth_year
        self.marital_status = marital_status.title()
        self.login_attempts = login_attempts
        
    def describe_user(self):
        print ("\nThe user's name is " + self.first_name + " " + self.last_name + ".")
        print (self.first_name + "'s mariatal status is " + self.marital_status + ".")
        print (self.first_name + " was born in " + str(self.birth_year) + ".")
        
    def greet_user(self):
        print ("\nThanks " + self.first_name + " for learning Python programming!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print (self.first_name + ", you reached the number of login attempts. Try again later!")
        
    def inform_login_attempts(self):
        print (self.first_name + "'s login attemp has failed - you have tryed " + str(self.login_attempts) + " times.")
        
#user_01 = User("Cassio","mendonca",1977,"married",0)
#inc = 3
#while inc != 0:
#    user_01.increment_login_attempts()
#    user_01.inform_login_attempts()
#    inc -= 1
#user_01.reset_login_attempts()
        
class Privileges():
    
    def __init__(self,first_name):
        """Inicializa a classe principal"""
        self.first_name = first_name
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        """Mostra os privilégios do admin"""
        message = "The Admin " + self.first_name + " has the following privileges: "
        for privilege in self.privileges:
            message += '"' + privilege.upper() + '", '
        print (message[:-2] + "!")
        
class Admin(User):
    """This class defines more privileges for the admin"""
    
    def __init__(self,first_name,last_name,birth_year,marital_status,login_attempts):
        """Inicializa a classe principal"""
        super().__init__(first_name,last_name,birth_year,marital_status,login_attempts)
        self.privileges = Privileges("Cassio")
    
ad = Admin("Cassio","mendonca",1977,"married",0)
ad.privileges.show_privileges()


