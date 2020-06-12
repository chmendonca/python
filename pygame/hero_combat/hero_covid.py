# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:04:32 2020
@author: Cassio
Description: This class was created as a container to the covid invaders on
the screen
"""

import pygame
from pygame.sprite import Sprite

class Covid(Sprite):
    """A class that represents a single covid on the 'air'"""
    
    def __init__(self,h_settings,screen):
        """Initializes the covid and sets its initial position"""
        super(Covid,self).__init__()
        self.screen = screen
        self.h_settings = h_settings
        
        #Uploads the image of the covid and defines its initial position
        self.image = pygame.image.load('images/covid_small.bmp')
        self.rect = self.image.get_rect()
        
        #Starts each single covid close to the right upper corner of the screen
        #The x position is the image width times its the number image width
        #   on the screen subtracted one, to set it not closed to the end of
        #   screen.
        self.rect.x = self.rect.width * \
                    (int(self.h_settings.screen_width / (self.rect.width)) - 1)
        self.rect.y = self.rect.height
        
        #Stores the exactly position of the covid
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draws the covid on its initial position"""
        self.screen.blit(self.image,self.rect)
        
    def check_edges(self):
        """Returs True if one covid reaches the edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0:
            return True
        elif self.rect.bottom >= screen_rect.bottom:
            return True
        
    def update(self):
        """Moves the alien to the bottom of screen"""
        self.y += (self.h_settings.covid_vertical_speed_factor *
                   self.h_settings.pandemy_direction)
        self.rect.y = self.y