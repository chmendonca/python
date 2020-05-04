# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 2020
@author: Cassio (chmendonca)
Description: This module will handle all the game functionalities that are not
necessary to be in the main module alien_invasion.py. It is better to make the
code clear and easier to understand
"""

import pygame
import sys

from hero_bullet import Bullet
from hero_covid import Covid

def fire_bullet(h_settings,screen,hero,bullets):
        """Shot the bullet if the limit has not been reached"""
        #Creates a new bullet and add it to the bullets group
        if len(bullets) < h_settings.bullets_allowed:
            new_bullet = Bullet(h_settings,screen,hero)
            bullets.add(new_bullet)

def check_keydown_events(event,h_settings,screen,hero,bullets):
    #Responds to key presses
    if event.key == pygame.K_RIGHT:
        #Moves the hero to right
        hero.moving_right = True
    elif event.key == pygame.K_LEFT:
        #Moves the hero to left
        hero.moving_left = True
    elif event.key == pygame.K_UP:
        #Moves the hero to up
        hero.moving_up = True
    elif event.key == pygame.K_DOWN:
        #Moves the hero to down
        hero.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(h_settings,screen,hero,bullets)
    elif event.key == pygame.K_q:
        pygame.display.quit()
        pygame.quit()
        sys.exit()
        
def check_keyup_events(event,hero):
    #Responds to key releases
    if event.key == pygame.K_RIGHT:
        hero.moving_right = False
    elif event.key == pygame.K_LEFT:
        hero.moving_left = False
    elif event.key == pygame.K_UP:
        hero.moving_up = False
    elif event.key == pygame.K_DOWN:
        hero.moving_down = False

def check_events(h_settings,screen,hero,bullets):
    """Watches and respond to keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,h_settings,screen,hero,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,hero)
        
                    
def update_screen(h_settings,screen,hero,bullets,covids):
    """Updaate the screen images and returns to the new screen"""
    #Redraw the screen every cycle
    screen.fill(h_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    hero.blitme()
    #covid.blitme() - used for a single covid on screen
    covids.draw(screen)
        
    #Updates the screen with the most recent graphics
    pygame.display.flip()
            
def update_bullets(bullets,screen):
    screen_rect = screen.get_rect()
    for bullet in bullets.copy():
        if bullet.rect.right >= screen_rect.right:
            bullets.remove(bullet)
    #print(len(bullets))

def get_number_covids_y(h_settings,covid_height):
    """Determines the number of covids in a column"""
    available_space_y = h_settings.screen_height - 2 * covid_height
    number_covids_y = int(available_space_y / (2 * covid_height))
    return number_covids_y

def get_number_columns(h_settings,hero_width,covid_width):
    #Determine the number of columns that fits on the screen
    available_space_x = (h_settings.screen_width - 
                         (1 * covid_width) - hero_width)
    number_columns = int(available_space_x / (2 * covid_width))
    return number_columns
    
def create_covid(h_settings,screen,covids,covid_height,covid_number,
                 column_number):
    """Creates a covid and set it on the column"""
    covid = Covid(h_settings,screen)
    covid.y = covid_height + 2 * covid_height * covid_number
    covid.rect.y = covid.y
    covid.rect.x = covid.rect.width + 2 * covid.rect.width * column_number
    covids.add(covid)
    
def create_fleet(h_settings,screen,hero,covids):
    """Creates a whole fleet of covids"""
    #Creates one covid and calculates the number of covids in one line
    #The space among covids is the height of one covid
    covid = Covid(h_settings,screen)
    covid_height = covid.rect.height
    number_covids_y = get_number_covids_y(h_settings,covid_height)
    number_columns = get_number_columns(h_settings,hero.rect.width,
                                        covid.rect.width)
    
    #Creates the first column of covids
    for column_number in range(number_columns - 3):
        column_number = number_columns - column_number
        print(column_number)
        for covid_number in range(number_covids_y):
            #Creates the covid and puts it on the column
            create_covid(h_settings,screen,covids,covid_height,covid_number,
                         column_number)