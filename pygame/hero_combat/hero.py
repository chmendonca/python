# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 2020
@author: Cassio (chmendonca)
Description: This class will have the hero characteristics and almost all
behaviors
"""

import pygame

class Hero():
    
    def __init__(self,h_settings,screen):
        """Initializes the hero on its initial position"""
        self.screen = screen
        self.h_settings = h_settings
        
        #Uploads the hero image and get the rect
        self.image = pygame.image.load('images/hero_small.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Starts the hero in the center of screen
        self.rect.left = 0
        self.rect.centery = self.screen_rect.centery
        
        #Stores a decimal value to the hero center
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        
        #Moving flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Updates the hero position depending on the moving flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right/5:
            self.center_x += self.h_settings.hero_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.h_settings.hero_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.h_settings.hero_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.h_settings.hero_speed_factor
            
        #Updates the rect object according to the self.center (x,y)
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y        
    
    def blitme(self):
        #Draw the image on the specified position
        self.screen.blit(self.image,self.rect)