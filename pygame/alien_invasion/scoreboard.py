#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame.font

class Scoreboard():
    """This class shows the player scores"""

    def __init__(self,ai_settings,screen,stats):
        """Initializes the scores attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #Configuring the scores font size
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #Configures the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Switches the score in an image"""
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,
                                            self.ai_settings.bg_color)

        #Shows the score on the right upper corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        """Switches the high score in an image"""
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)

        #Centralizes the highest score in the top center of the page
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Switches the level number in an image"""
        self.level_image = self.font.render(str(self.stats.level),True,self.text_color,self.ai_settings.bg_color)
        self.level_level = self.font.render("LEVEL",True,self.text_color,self.ai_settings.bg_color)

        #Shows the level under the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        self.level_level_rect = self.level_level.get_rect()
        self.level_level_rect.right = self.level_rect.left - 20
        self.level_level_rect.top = self.level_rect.top

    def show_score(self):
        """Draws the score on screen"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.screen.blit(self.level_level,self.level_level_rect)