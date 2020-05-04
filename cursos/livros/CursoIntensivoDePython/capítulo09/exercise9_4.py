# -*- coding: utf-8 -*-
"""
Chapter 9 - Classes (Ex. 9.4 - page 232)
Book: Curso Intensivo de Python
Date: 20Apr2020
"""

#exercise 9.4
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print ("\nThe restaurant's name is " + self.restaurant_name + ".")
        print ("It's cuisine is specialized in " + self.cuisine_type + " food.")
        
    def open_restaurant(self):
        print ("The restaurant is open now.")
    
    def served(self):
        print ("The number of guests attended was " + str(self.number_served))
        
    def set_number_served(self,number):
        self.number_served = number
        self.served()
        
    def increment_number_served(self,number):
        self.number_served += number
        self.served()
        
restaurant_01 = Restaurant("Outback", "barbecue")
restaurant_01.describe_restaurant()
restaurant_01.open_restaurant
restaurant_01.served()
restaurant_01.set_number_served(10)
restaurant_01.increment_number_served(25)

