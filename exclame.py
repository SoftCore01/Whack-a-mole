

import pygame
from mole import Mole

class Exclame:

    def __init__(self,game) -> None:

        # Load in game settings
        self.setting = game.setting
        self.screen = game.screen

        # Load in image and rectangle
        self.image = pygame.image.load("wackamole\\game image files\\backgroundless game images\\impact_exclamations-removebg-preview.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.status = False

    def display(self):
        if self.status:
            self.screen.blit(self.image,self.rect)
