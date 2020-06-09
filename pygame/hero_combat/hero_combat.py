# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:36:20 2020
@author: Cassio
Description: This "Hero Combat 19" game was created for fun and to reinforce
the learnings I've had when studng "pygame" tool to develop games (and possible 
apps). At this game, the player will control the Hero in the four directions 
(including diagonals) and shot bullets (vacine serynges) on COVID-19 pandemy 
that plagues the World (2020 quarentine).
    The pandemy moves over the Hero that uses the shots to destroy each virus.
The virus pandemy moves up and down (or vice-versa) and to left. Every time
that the hero destroys one advance of pandemy, a new challenge will takeover. 
In case of one COVID-19 to infect the hero, the Hero will "loose" part of its
imunity. After being infected by 3 COVID-19 the Hero will die and the game will
over!
"""

from pygame.sprite import Group

import pygame

from hero import Hero
from hero_button import Button
from hero_game_stats import GameStats
from hero_settings import Settings

import hero_game_functions as hgf

#from hero_covid import Covid

def run_game():
    """Initializing game conditions and configurationes"""
    pygame.init()
    h_settings = Settings()
    screen = pygame.display.set_mode((h_settings.screen_width,
                                      h_settings.screen_height))
    pygame.display.set_caption('HERO COMBAT')
    
    #Creates a start button
    play_button = Button(h_settings,screen,"PLAY")
    
    #Creates an instance to store the game statistics
    stats = GameStats(h_settings)
    
    
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
        if stats.game_active:
            hgf.check_events(h_settings,screen,stats,h,bullets,covids,play_button)
            h.update()
            bullets.update()
            hgf.update_bullets(h_settings,screen,h,covids,bullets)
            hgf.update_covids(h_settings,stats,screen,h,covids,bullets)
        else:
            bullets.empty()
            covids.empty()
            hgf.check_events(h_settings,screen,stats,h,bullets,covids,play_button)
            
        hgf.update_screen(h_settings,stats,screen,h,covids,bullets,play_button)
        
run_game()