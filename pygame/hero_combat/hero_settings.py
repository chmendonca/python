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
        self.screen_width = 1000
        self.screen_height = 580
        self.bg_color = (0,20,50)
        
        #Increase of ship speed to 1.5 pixels instead of 1
        self.hero_speed_factor = 1.5
        
        #Configuring the syringes (bullets)
        self.bullet_speed_factor = 1
        self.bullets_allowed = 50