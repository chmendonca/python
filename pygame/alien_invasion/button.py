# -*- coding: utf-8 -*-
"""
Created on Wed May  6 08:47:35 2020
@author: Cassio (chmendonca)
Description: This class will have the details to insert a button to start
    playing the game
"""

import pygame.font

class Button():
    
    def __init__(self,ai_settings,screen,msg):
        """Initializes the button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #Define the dimensions and propertys of the button
        self.width,self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255) #white
        self.font = pygame.font.SysFont(None,48)
        
        #Build the rect object of the button and centralizes it
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        
        #The button message is bouit only once
        self.prep_msg(msg)
        
    def prep_msg(self,msg):
        """Transform the msg on renderized image and sets it at the center of
            the button"""
        self.msg_image = self.font.render(msg,True,self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        #Draws a white button then fill it with the msg and the properties
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)