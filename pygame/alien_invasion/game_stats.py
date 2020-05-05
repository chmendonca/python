#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:39:23 2020
@author: Cassio (chmendonca)
Description: This class is used to store game statistics for scores
"""

class GameStats():
    """Stores the statistic data of the game"""
    
    def __init__(self,ai_settings):
        """Initializes the stats data"""
        self.ai_settings = ai_settings
        self.ships_left = self.ai_settings.ship_limit
        self.reset_stats(0)
        
        #Initializes the game in an active state
        self.game_active = True
        
        print('initialized')
        
    def reset_stats(self,limit):
        """Initializes the stats data that could change during the game"""
        self.ships_left = self.ships_left+limit
        print(self.ships_left)
#        ships_left = self.ships_left
#        return ships_left