# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 2020
@author: Cassio (chmendonca)
Description: This module will handle all the game functionalities that are not
necessary to be in the main module alien_invasion.py. It is better to make the
code clear and easier to understand
"""

from time import sleep

import pygame
import sys

from alien import Alien
from bullet import Bullet

def fire_bullet(ai_settings,screen,ship,bullets):
    #Creates a new bullet and inserts it on the Group
    #Limits the number of bullets per window
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet= Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    #Responds to key presses
    if event.key == pygame.K_RIGHT:
        #Moves the spaceship to right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #Moves the spaceship to left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        pygame.display.quit()
        pygame.quit()
        sys.exit()

def check_keyup_events(event,ship):
    #Responds to key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    """Watches and respond to keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Issue2
            pygame.display.quit()
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        
                    
def update_screen(ai_settings,screen,ship,bullets,aliens):
    """Updaate the screen images and returns to the new screen"""
    #Redraw the screen every cycle
    screen.fill(ai_settings.bg_color) #Issue3
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
        
    #Updates the screen with the most recent graphics
    pygame.display.flip()
    
def check_bullet_alien_collisions(ai_settings,screen,ship,bullets,aliens):
    #Verifies if any bullet has strike any alien. If yes, destroys the bullet
    #   and the alien.
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    
    if len(aliens) == 0:
        #Detroys the bullets not used after vanishing the fleet and creates a
        #   new fleet
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        
def update_bullets(ai_settings,screen,ship,aliens,bullets):        
    """Updates the bullets position and vanish the old ones"""
    #Vanish the bullets that have gone upper on the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
#        #print(len(bullets))python
            
    check_bullet_alien_collisions(ai_settings,screen,ship,bullets,aliens)

def get_number_aliens_x(ai_settings,alien_width):
    #Determines the number of aliens per line
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """Determines the number of aliens rows on the screen"""
    available_space_y = (ai_settings.screen_height - 
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,alien_width,row_number):
    #Creates an alien and alocates it on the line
    alien = Alien(ai_settings,screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
        
def create_fleet(ai_settings,screen,ship,aliens):
    """Crates the complete alien fleet"""
    #Creates the first alien and calculates how many more per line
    #The space between each alien is the same width of the alien
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings,alien_width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,
                                  alien.rect.height)

    #Creates the first line of aliens
    for row_number in range(number_rows):
        for alien_number in range (number_aliens_x):
            #Creates an alien and alocates it in line with others
            create_alien(ai_settings,screen,aliens,alien_number,alien_width,row_number)

def check_fleet_edges(ai_settings,aliens):
    """Acts when any alien touches the screen edges"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_directions(ai_settings,aliens)
            break

def change_fleet_directions(ai_settings,aliens):
    """Makes the whole fleet to go down and swtich its direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,screen,ship,bullets,aliens):
    """Returns when the spaceship is hit by an alien"""
    #Decreases ship_left
    stats.reset_stats(-1)
    
    #Makes a short pause to allow the player observes that the spaceship has
    #   been hit
    sleep(0.5)
    
    #Empty the aliens and bullets lists
    aliens.empty()
    bullets.empty()
    
    #Creates a new fleet and centralizes the spaceship
    create_fleet(ai_settings,screen,ship,aliens)
    ship.center_ship()
    
    #Makes a pause before starting again
    sleep(5)
    
def check_aliens_bottom(ai_settings,stats,screen,ship,bullets,aliens):
    """Verifies if an alien reached the end of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Do the same for the spaceship has been hit
            ship_hit(ai_settings,stats,screen,ship,bullets,aliens)
            break
        
def update_aliens(ai_settings,stats,screen,ship,bullets,aliens):
    """Verifies if the fleet reached one edge and updates the positions of all
        aliens in the fleet"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    
    #Verifies if there is a colision between aliens and spaceship
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,bullets,aliens)
        
    #Verifies if any alien has reached the bottom of the screen
    check_aliens_bottom(ai_settings,stats,screen,ship,bullets,aliens)
    