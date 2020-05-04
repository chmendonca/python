# -*- coding: utf-8 -*-
"""
Chapter 9 - Classes (Example pages 233 until 242)
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
        
    def fill_gas_tank(self):
        """Indicates to the user that it is necessary to fill the gas tank"""
        print ("The fuel tank is almost empty, go to next gas station")
        
        
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

class Battery():
    """Uma tentativa simples de moderla uma bateria para um carro elétrico"""
    
    def __init__(self, battery_size = 85):
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria"""
        print ("This car has a " + str(self.battery_size) + "kWh battery. - Battery()")
        
    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria"""
        if self.battery_size == 70:
            distance = 240
        elif self.battery_size == 85:
            distance = 270
        
        message = "This car can go approximately " + str(distance)
        message += " miles on a full charge."
        print (message)
        



#page 233
class ElectricCar(Car):
    """Representa apspectos de um carro específicos de veículos elétricos"""
    
    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai
        Em seguida inicializa os atributos específicos de um carro elétrico
        """
        super().__init__(make, model, year)
        #page 235
        self.battery_size = 70
        self.battery = Battery()
            
    #page 235
    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria"""
        print ("This car has a " + str(self.battery_size) + "kWh battery. - ElectricCar()")
        
    #page 237
    def fill_gas_tank(self):
        """Carros elétricos não têm tanques de gasolina"""
        print ("This car doesn't need gas tank!")
        
#my_tesla = ElectricCar("tesla","model s", 2016)
#print (my_tesla.get_descriptive_name())
#
##page 235
#my_tesla.describe_battery()
#
##page 237
#my_tesla.fill_gas_tank()
#
#my_tesla.battery.describe_battery()
#
#my_tesla.battery.get_range()