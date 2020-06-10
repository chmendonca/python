# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 2020
@author: Cassio (chmendonca)
Description: This class was created as a container to the game characteristics
and configurations
"""

class Settings():
    """A class that have all configurations of the game"""
    
    def __init__(self):
        """Initialize the game static configs"""
        #Screen configuration
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (230,230,230)
        
        #Spaceship configuration
        #Increase of ship speed to 1.5 pixels instead of 1
        #self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        #Bullets configuration
        #self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3
        
        #Alien configuration
        #self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction = 1 means to the right; -1 means to the left
        #self.fleet_direction = 1

        #Game speed increment
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initializes the configs that change during the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet_direction = 1 means to the right; -1 means to the left
        self.fleet_direction = 1

        #Alien Score
        self.alien_points = 50

    def increase_speed(self):
        """Increase the speed configurations"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale