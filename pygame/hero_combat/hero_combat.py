# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:36:20 2020
@author: Cassio
Description: Exercises 12.1 and 12.2
"""

import pygame

from hero import Hero
from hero_settings import Settings
from pygame.sprite import Group
import hero_game_functions as hgf

#from hero_covid import Covid

def run_game():
    """Initializing game conditions and configurationes"""
    pygame.init()
    h_settings = Settings()
    screen = pygame.display.set_mode((h_settings.screen_width,
                                      h_settings.screen_height))
    pygame.display.set_caption('HERO COMBAT')
    
    #Creates a hero instance
    h = Hero(h_settings,screen)
    
    #Creates a group to store the bullets
    bullets = Group()
    covids = Group()
    
    #Creates the covid
    #This is no longer used. It was used to create a single covid on the screen
    #   to determine its initial position. It was replaced by covids group and
    #   fleet.
    #covid = Covid(h_settings,screen)
    
    #Creates the covid fleet
    hgf.create_fleet(h_settings,screen,h,covids)
    
    #Start the main loop
    while True:
        hgf.check_events(h_settings,screen,h,bullets)
        h.update()
        bullets.update()
        hgf.update_bullets(bullets,screen)        
        hgf.update_screen(h_settings,screen,h,bullets,covids)
        
run_game()