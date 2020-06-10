# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:38:01 2020
@author: Cassio (chmendonca)
Description: At Alien Invasion, the player controls a spaceship that is placed
on the bottom of the screen. The player has the ability to move the spaceship
left and right using the key arrows and the space bar to shot. When the game
starts, the sky is filled with an alien fleet that moves left and right then
down. The player shots the aliens to destroy them. Every time that the player
destroys a complete fleet, a new one, faster than the previous, will take place
on the sky. In case of any alien to touch the player space ship or touches the
ground (the bottom of screen), the player will loose one spaceship (life).
After loosing three spaceships (all lifes), the game will over. 
"""

from pygame.sprite import Group

import pygame

from button import Button
from game_stats import GameStats
from settings import Settings
from scoreboard import Scoreboard
from ship import Ship

import game_functions as gf 

def run_game():
    #Initialize the game and creates the objects for the screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height)) #Issue1
    pygame.display.set_caption("Alien Invasion")
    
    #Creates the play button
    play_button = Button(ai_settings,screen,"Play")
    
    #Creates an instance to store the statistic data from the game and the scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    #creates a spaceship (instance)
    ship=Ship(ai_settings,screen)
    
    #Creates a group to allocate the bullets and aliens
    bullets = Group()
    aliens = Group()
    
    #Creates an alien fleet
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    #Starts the game main loop
    while True:
        gf.check_events(ai_settings,stats,screen,ship,aliens,bullets,play_button,sb)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings,stats,screen,ship,aliens,bullets,sb)
            gf.update_aliens(ai_settings,stats,screen,ship,bullets,aliens,sb)
        else:
            aliens.empty()
            bullets.empty()
        gf.update_screen(ai_settings,screen,stats,ship,bullets,aliens,
                         play_button,sb)
    
run_game()
