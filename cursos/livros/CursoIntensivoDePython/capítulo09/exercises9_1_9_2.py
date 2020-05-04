# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Chapter 9 - Classes (Ex. 9.1/9.2 - pages 225,226)
Book: Curso Intensivo de Python
Date: 20Apr2020
"""

#exercise 9.1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print ("\nThe restaurant's name is " + self.restaurant_name + ".")
        print ("It's cuisine is specialized in " + self.cuisine_type + " food.")
        
    def open_restaurant(self):
        print ("The restaurant is open now.")
        
restaurant_01 = Restaurant("Outback", "barbecue")
restaurant_01.describe_restaurant()
restaurant_01.open_restaurant

#exercise 9.2
restaurant_02 = Restaurant("Apple Bee's", "general")
restaurant_03 = Restaurant("Digao","brazilian")

restaurant_01.describe_restaurant()
restaurant_02.describe_restaurant()
restaurant_03.describe_restaurant()

