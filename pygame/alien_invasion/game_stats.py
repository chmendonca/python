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

        #The highest score will never be reinitialized
        self.high_score = 0
        
        #Initializes the game in an inactive state
        #It will allow to insert some information on the screen before the
        #   playing the game, such as a "play button" to start the game
        self.game_active = False
        
        self.reset_stats(0)
        
    def reset_stats(self,limit):
        """Initializes the stats data that could change during the game"""
        self.ships_left = self.ships_left+limit
        #print(self.ships_left)
#        ships_left = self.ships_left
#        return ships_left
        if not self.game_active:
            self.score = 0
            self.ships_left = 3
            self.level = 1