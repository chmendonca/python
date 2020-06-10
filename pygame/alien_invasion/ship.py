# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 2020
@author: Cassio (chmendonca)
Description: This class will have the ship characteristics and almost all
behaviors
"""

import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        """Initializes the spaceship and defines its initial position"""
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #Uploads the spaceship image and gets its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Initializes the spaceship on the center bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #Stores a decimal value to the spaceship center
        self.center = float(self.rect.centerx)
        
        #Moving Flags
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Updates the spaceship position depending on the moving flag"""
        #Updates the spaceship position, not the rectangle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        #Updateds the rect object according to the self.center
        self.rect.centerx = self.center
        
    def blitme(self):
        """Sets the spaceship at initial position"""
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        """Sets the spaceship on the center of the screen"""
        self.center = self.screen_rect.centerx