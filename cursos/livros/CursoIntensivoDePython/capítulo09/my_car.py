# -*- coding: utf-8 -*-
"""
Chapter 9 - Classes (Example pages 243 to)
Book: Curso Intensivo de Python
Date: 20Apr2020
"""

from car import Car

my_new_car = Car("audi","a4",2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 20
my_new_car.read_odometer()