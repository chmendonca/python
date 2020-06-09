# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 2020
@author: Cassio (chmendonca)
Description: This class was created as a container to the game characteristics
and configurations
"""
from random import randint

class Settings():
    """A class that have all configurations of the game"""
    
    def __init__(self):
        """Initialize the game configs"""
        #Screen configuration
        self.screen_width = 1100
        self.screen_height = 680
        self.bg_color = (0,20,50)
        
        #Hero configuration
        #Increase of ship speed to 1.5 pixels instead of 1
        self.hero_speed_factor = 1.5
        self.hero_limit = 2
        
        #Syringes (bullets) configuration
        self.bullet_speed_factor = 1
        self.bullets_allowed = 50
        
        #Covids configuration
        self.covid_vertical_speed_factor = 1
        #The value of the movement is negative because it is increasing
        #   from the right to the left
        self.covid_horizontal_speed_factor = -100
        #The pandemy direction equals 1 means to the bottom; -1 means to the top
        #The randint ensures an randomly when starting the game
        if randint(0,1) == 1:
            self.pandemy_direction = 1
        else:
            self.pandemy_direction = -1