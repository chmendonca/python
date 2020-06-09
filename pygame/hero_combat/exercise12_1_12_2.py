# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:36:20 2020
@author: Cassio
Description: Exercises 12.1 and 12.2
"""

import pygame
import sys

from hero import Hero

def run_game():
    """Initializing game conditions and configurationes"""
    pygame.init()
    screen = pygame.display.set_mode((800,500))
    pygame.display.set_caption('HERO')
    bg_color = (0,240,220)
    hero = Hero(screen)
    
    #Start the main loop
    while True:
        
        #Watches and respond to keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                
        #Set the screen background color
        screen.fill(bg_color)
        hero.blitme()
        
        #Set the most recent screen
        pygame.display.flip()
        
run_game()