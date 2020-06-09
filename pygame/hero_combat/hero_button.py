# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 13:33:07 2020

@author: Cassio
"""

import pygame.font

class Button():
    
    def __init__(self,ai_settings,screen,msg):
        """Initializes the button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #Define the button properties and dimensions
        self.width, self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48,1)
        
        #Implements the button object rect and centralizes it
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        
        #The button message should be created only once
        self.prep_msg(msg)
        
    def prep_msg(self,msg):
        """Transforms the text msg in an renderized image and centrilizes
        the button text"""
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        #Draws a clean button and after draws the message
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
        