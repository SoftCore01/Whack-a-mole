

import pygame
from colors import *
pygame.init()

class Settings:
    """This class contains the settings for the whack-a-mole game"""

    def __init__(self):
        """ This initializes the settins class"""

        self.size = self.width,self.height = 600,400
        self.bg_color = (150,200,0)

        #self.screen = pygame.display.set_mode(self.size)
        self.mole_time = 2000
        self.mole_delay = 3
        self.mole_point = 10

        self.initial_game_time = 10
        self.game_time = self.initial_game_time
