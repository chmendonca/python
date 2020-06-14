# -*- coding: utf-8 -*-
 
import pygame.font

from hero import HeroLives
from pygame.sprite import Group


class Scoreboard():
    """This class shows data about scores and hero lives"""
    def __init__(self,hero_settings,screen,stats):
        """Initializes the scores attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.hero_settings = hero_settings
        self.stats = stats

        #Scores font configuration
        self.text_color = (0,255,00)
        self.font_score = pygame.font.SysFont(None,42,1)
        self.font_high_score = pygame.font.SysFont(None,48,1)
        self.font_level = pygame.font.SysFont(None,36)

        #Configures the initial score image
        self.prep_high_score()
        self.prep_score()
        self.prep_level()
        self.prep_hero_lives()

    def prep_score(self):
        """Changes the score string in an image"""
        score_str = str(self.stats.score)
        self.score_image = self.font_score.render(score_str,True,self.text_color,self.hero_settings.bg_color)

        #Shows the score on the left upper side of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 10
        self.score_rect.top = self.high_score_rect.bottom #sets the score under the high score
    
    def prep_high_score(self):
        """Switches the highest score string in an image"""
        high_score = int(round(self.stats.high_score,1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font_high_score.render(high_score_str,True,self.text_color,
            self.hero_settings.bg_color)
        
        #Shows the highest score on the left top score of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 10
        self.high_score_rect.top = 20
    
    def prep_level(self):
        """Changes the level score string in an image"""
        self.level_level_image = self.font_level.render("LEVEL:",True,self.text_color,self.hero_settings.bg_color)
        self.level_image = self.font_level.render(str(self.stats.level),True,self.text_color,self.hero_settings.bg_color)

        #Sets the level at left bottom corner
        self.level_level_rect = self.level_level_image.get_rect()
        self.level_level_rect.left = self.screen_rect.left + 10
        self.level_level_rect.bottom = self.screen_rect.bottom - 10
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.level_level_rect.right + 10
        self.level_rect.bottom = self.screen_rect.bottom - 10

    def prep_hero_lives(self):
        """Shows how many lives the hero has"""
        self.hero_lives = Group()
        for hero_lives_number in range(self.stats.heros_left):
            hero_live = HeroLives(self.hero_settings,self.screen)
            hero_live.rect.x = self.screen_rect.right - 80 + hero_lives_number * hero_live.rect.width
            hero_live.rect.y = 10
            self.hero_lives.add(hero_live)

    def show_score(self):
        """Shows the score on the screen"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_level_image,self.level_level_rect)
        self.screen.blit(self.level_image,self.level_rect)
        
        #Draws the hero lives
        self.hero_lives.draw(self.screen)