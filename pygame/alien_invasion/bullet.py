# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 08:45:24 2020
@author: Cassio (chmendonca)
Description: This class will have the bullets characteristics and behaviors
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """This class configures the bullets shot by spaceship"""
    
    def __init__(self, ai_settings,screen,ship):
        """Creates a bullet on the spaceship actual position"""
        super(Bullet,self).__init__()
        self.screen = screen
        
        #Creates a new rectangle for the bullet in a fixed position (0,0) then
        # sets the correct position on spaceship position
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """Moves the bullet to the top of the screen"""
        #Updates the bullet position
        self.y -= self.speed_factor
        self.rect.y = self.y        
        
    def draw_bullet(self):
        """Draws the bullet on screen"""
        pygame.draw.rect(self.screen, self.color,self.rect)
        
        