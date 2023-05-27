



import pygame
from pygame.sprite import Sprite
from colors import *
pygame.init()



class Mallet(Sprite):
    """This class contains the settings for the whack-a-mole game"""

    def __init__(self,game):
        """ This initializes the settins class"""
        super().__init__()

        # Load in game settings
        self.setting = game.setting

        # Load in mallet image and rect
        self.image = pygame.image.load('wackamole\\game image files\\backgroundless game images\\wooden-mallet-vector-9524930-removebg-preview.png')
        self.rect = self.image.get_rect()

        # Scale the mallet rect to improve impact detection
        self.rect.scale_by_ip(0.4,1)
