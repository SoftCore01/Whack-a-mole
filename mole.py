

import pygame
from pygame.sprite import Sprite
from colors import *
import random
import time
pygame.init()



class Mole(Sprite):
    """This class contains the settings for the whack-a-mole game"""

    def __init__(self,game,*groups):
        """ This initializes the settins class"""
        super().__init__(*groups)
        # Load in game settings
        self.setting = game.setting
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.time = None

        # Load game images and rectangle
        self.image = pygame.image.load('wackamole\\game image files\\backgroundless game images\\mole-removebg-preview.png')
        self.rect = self.image.get_rect()
        self.rect.scale_by_ip(0.5,0.5)
        self.x = self.rect.x
        self.y = self.rect.y
        self.x_list = [self.screen_rect.centerx-70,self.screen_rect.centerx,self.screen_rect.centerx+70]
        self.y_list = [self.screen_rect.centery-70,self.screen_rect.centery,self.screen_rect.centery+70]
        self.rect.centerx = random.choice(self.x_list)
        self.rect.centery = random.choice(self.y_list)

        #self.time_stamp = None


    def update(self):
        if self.time is not None:
            #print(f'The mole time is {self.time}')
            if pygame.time.get_ticks()-self.time >= self.setting.mole_time:
                #print(f'The time difference is{self.time_stamp-self.time}')
                #print('Mole killed')
                self.kill()




    #def __del__(self):
    #    print('destroyed')

#        Load in exclame image,rect and status
#        self.exclame = pygame.image.load("wackamole\\game image files\\backgroundless game images\\impact_exclamations-removebg-preview.png")
#        self.exclame_rect = self.exclame.get_rect()
#        self.exclame_rect.x,self.exclame_rect.y = self.rect.x-60,self.rect.y-50
#        self.exclame_status = False
