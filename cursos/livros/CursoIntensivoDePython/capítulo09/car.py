# -*- coding: utf-8 -*-
"""
Chapter 9 - Classes (Example pages 226 until 242)
Book: Curso Intensivo de Python
Date: 20Apr2020
"""

class Car():
    #page 226
    """Uma tentativa simples de representar um carro"""
    
    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro"""
        self.make = make.upper()
        self.model = model.title()
        self.year = year
        #page 228
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    
    #page 228
    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro"""
        print ("This car has " + str(self.odometer_reading) + " miles on it.")
        
    #page 229
    def update_odometer(self,mileage):
        """Define o valor de leitura do hodometro com o valor especificado
           Rejeita a alteracao se for tentativa de definir um valor menor para o hodometro
        """
        #page 230
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print ("You can't roll back an odometer!")
    
    #page 231
    def increment_odometer(self,miles):
        """Soma a quantidade especificada ao valor de leitura do hodometro"""
        self.odometer_reading += miles
        
        
#my_new_car = Car("audi","a4",2016)
#print (my_new_car.get_descriptive_name())
##page 228
#my_new_car.read_odometer()
##page 229
#my_new_car.odometer_reading = 23
#my_new_car.read_odometer()
##page 229
#my_new_car.update_odometer(32)
#my_new_car.read_odometer()
##page 230
#my_new_car.update_odometer(22)
#my_new_car.read_odometer()
#
##page 231
#print ("\n")
#my_used_car = Car("subaru","outback",2013)
#print(my_used_car.get_descriptive_name())
#
#my_used_car.update_odometer(23500)
#my_used_car.read_odometer()
#
#my_used_car.increment_odometer(100)
#my_used_car.read_odometer()

