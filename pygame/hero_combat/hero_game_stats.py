# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:36:28 2020
@author: Cassio (chmendonca)
Description: This class contains the means to define and to store stats data
    to/from game
"""

class GameStats():
    """Stores the game statistics data"""
    
    def __init__(self,h_settings):
        """Initializes the statistic data"""
        self.h_settings = h_settings
        self.reset_stats()
        
        #Initializes the Hero Combat in inactive state
        self.game_active = False

        #Restarting highest score
        self.high_score = 0
        
    def reset_stats(self):
        """Initializes the statistic data that can change during the game"""
        self.heros_left = self.h_settings.hero_limit
        self.score = 0
        self.level = 1