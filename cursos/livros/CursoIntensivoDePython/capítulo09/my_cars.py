# -*- coding: utf-8 -*-
"""
Chapter 9 - Classes (Example pages 245 to)
Book: Curso Intensivo de Python
Date: 20Apr2020
"""

#from electric_car import Car, ElectricCar
#import electric_car

from car import Car
from electric_car import ElectricCar

my_beetle = Car("volkswagen", "beetle",2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla","model s",2016)
print(my_tesla.get_descriptive_name())
my_tesla.odometer_reading = 20
my_tesla.read_odometer()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()