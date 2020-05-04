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
        """Initialize the game configs"""
        #Screen configuration
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (230,230,230)
        
        #Increase of ship speed to 1.5 pixels instead of 1
        self.ship_speed_factor = 1.5
        
        #Configurating the bullets
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3
        

