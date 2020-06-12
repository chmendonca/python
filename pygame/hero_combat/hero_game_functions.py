# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 2020
@author: Cassio (chmendonca)
Description: This module will handle all the game functionalities that are not
necessary to be in the main module alien_invasion.py. It is better to make the
code clear and easier to understand
"""

from random import randint
from time import sleep
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
        
def check_play_button(h_settings,screen,stats,play_button,hero,covids,bullets,
                      mouse_x,mouse_y):
    """Starts a new game when the player hits the start button"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #Restarts the game initial conditions
        h_settings.initialize_dynamic_settings()
        
        #Hidden the mouse arrow
        pygame.mouse.set_visible(False)
        #Reinitializes the game stats and data
        stats.reset_stats()
        stats.game_active = True
        
        #Empty the covids and vacines lists
        covids.empty()
        bullets.empty()
        
        #Creates a new pandemy and centralizes the hero
        #create_fleet(h_settings,screen,hero,covids)
        hero.center_hero()

def check_events(h_settings,screen,stats,hero,bullets,covids,play_button):
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
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(h_settings,screen,stats,play_button,hero,covids,bullets,
                      mouse_x,mouse_y)
                    
def update_screen(h_settings,stats,screen,hero,covids,bullets,play_button):
    """Updaate the screen images and returns to the new screen"""
    #Redraw the screen every cycle
    screen.fill(h_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    hero.blitme()
    #covid.blitme() - used for a single covid on screen
    covids.draw(screen)
    
    #Draws the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()
        
    #Updates the screen with the most recent graphics
    pygame.display.flip()
    
def check_bullet_covid_collisions(h_settings,screen,hero,covids,bullets):
    #Verifies if the bullet has hit the covid. If yes, destroy the covid and 
    #   the bullet
    collisions = pygame.sprite.groupcollide(bullets,covids,True,True)
    
    #Delete the missing bullets and creates a new pandemy when the existent one
    #   is desinfected.
    if len(covids) == 0:
        bullets.empty()
        h_settings.increase_speed()
        create_fleet(h_settings,screen,hero,covids)    

            
def update_bullets(h_settings,screen,hero,covids,bullets):
    """Updates the bullets position, vanish the old ones and avoid overlap"""
    #Gets the screen rect
    screen_rect = screen.get_rect()
    
    #Creates empty lists for bullets rects
    bullets_rect_right_list = []
    bullets_rect_left_list = []
    
    for bullet in bullets.copy():
        
        #Removes overlaps among bullets and ensure a minimal distance between
        #   them
        #Adds the bullets rects in lists
        bullets_rect_left_list.append(bullet.rect.left)
        bullets_rect_right_list.append(bullet.rect.right)
        if len(bullets_rect_left_list) > 1:
            #if there is an overlap between the previous bullet plus 50 pixels
            #   removes the bullet from the list
            if bullets_rect_right_list[-1] >= bullets_rect_left_list[-2] - 50:
                bullets.remove(bullet)
        
        #Vanishes the bullets that overpass the right side of the screen
        if bullet.rect.right >= screen_rect.right:
            bullets.remove(bullet)
    #print(len(bullets))
    
    check_bullet_covid_collisions(h_settings,screen,hero,covids,bullets)

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
        
        #empty list to register the previous covid positions
        covid_number_position=[]
        #for covid_number in range(number_covids_y):
        for _ in range(number_covids_y):
            #Creates the covid and puts it on the column
            #Random number between 0 and number_covids_y-1
            covid_position = randint(0,number_covids_y-1)
            #To ensure that the position is empty before creating the covid
            #   in that position
            if covid_position not in covid_number_position:
                covid_number_position.append(covid_position)
                create_covid(h_settings,screen,covids,covid_height,
                             covid_position,column_number)

def check_pandemy_edges(h_settings,covids):
    """Returns if any covid has reached the edge"""
    for covid in covids.sprites():
        if covid.check_edges():
            change_pandemy_direction(h_settings,covids)
            break
        
def change_pandemy_direction(h_settings,covids):
    """Makes the complete fleet goes left and change its direction (up or down)"""
    for covid in covids.sprites():
        covid.rect.x += h_settings.covid_horizontal_speed_factor
    h_settings.pandemy_direction *= -1
    
def hero_hit(h_settings,stats,screen,hero,covids,bullets):
    """Returns if the hero has been hit by covids"""
    #Decreases the number of hero lifes
    if stats.heros_left > 0:
        stats.heros_left -= 1
        print(stats.heros_left)
        
        #Sleeps to give time to the player see what happened
        sleep(2)
        
        #Empty the covids and bullets from the screen
        covids.empty()
        bullets.empty()
        
        #Creates a new fleet and centralize the hero
        create_fleet(h_settings,screen,hero,covids)
        hero.center_hero()
        
        #Sleeps
        sleep(0.5)
    
    else:
        stats.game_active = False
        #This command makes the mouse visible after the game is finished (it was 
        # hidden wehn the play_button was hit)
        pygame.mouse.set_visible(True)
        sleep(0.5)
    
def check_covids_right(h_settings,stats,screen,hero,covids,bullets):
    """Verify if any covid has reached the right side of the screen"""
    screen_rect = screen.get_rect()
    for covid in covids.sprites():
        if covid.rect.left < screen_rect.left:
            #Makes the same for covid hitting hero
            hero_hit(h_settings,stats,screen,hero,covids,bullets)
            break
    
def update_covids(h_settings,stats,screen,hero,covids,bullets):
    """Verifies if at least one covid of the pandemy has reachead the screen
        edge and updates the positions of all covids on the pandemy"""
    check_pandemy_edges(h_settings,covids)
    covids.update()
    
    #Verifies if there is a collision between any covid and the Hero
    if pygame.sprite.spritecollideany(hero,covids):
        hero_hit(h_settings,stats,screen,hero,covids,bullets)
        
    #Verifies if any covid has reached the left border of the screen
    check_covids_right(h_settings,stats,screen,hero,covids,bullets)