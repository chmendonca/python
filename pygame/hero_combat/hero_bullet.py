# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:59:40 2020
@author: Cassio (chmendonca)
Description: This class will have the bullets characteristics and behaviors
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ The class that controls the bullets shot by hero"""
    
    def __init__(self,h_settings,screen,hero):
        """Creates the object for the bullet from the actual hero position"""
        super(Bullet,self).__init__()
        self.screen = screen
        
        #Uploads the syringe image and get the rect
        self.image = pygame.image.load('images/syringe_default.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        
        #Since in this project it will be used an image to be shot as a bullet,
        # it is not necessary to create the bullet position, but only to set
        # its correct position from the hero
        self.rect.centery = hero.rect.centery
        self.rect.right = hero.rect.right
        
        #Stores the bullet position as decimal value
        self.x = float(self.rect.x)
        
        #It is not necessary to define color because it is a predefined image
        
        #Setting the bullet speed
        self.speed_factor = h_settings.bullet_speed_factor
        
    def update(self):
        """Moves the bullet to the rigth"""
        #Updates the decimal position of the bullet
        self.x += self.speed_factor
        #Updates the rectangle position
        self.rect.x = self.x
        return self.x
        
    def draw_bullet(self):
        """Draws the bullet on the screen"""
        self.screen.blit(self.image,self.rect)
        