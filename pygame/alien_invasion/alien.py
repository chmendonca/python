# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 2020
@author: Cassio (chmendonca)
Description: This class will have the ship characteristics and almost all
behaviors
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class that represents a single alien from the fleet"""
    
    def __init__(self,ai_settings,screen):
        """Initializes the alien and defines its initial position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #Loads the alien image and defines its rectangle (rect)
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #Starts each alien at the left upper corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Stores the alien exactly position
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draws the alien on its original position"""
        self.screen.blit(self.image,self.rect)
        
    def check_edges(self):
        """Returns True if one alien is at any edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True
        
    def update(self):
        """Moves the alien to the right or to the left"""
        self.x += (self.ai_settings.alien_speed_factor * 
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
        