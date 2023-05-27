

import pygame
pygame.init()

class Hole:
    """Class that initializes and manages mole holes"""
    
    def __init__(self,game):
        
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.image = pygame.image.load("C:\\Users\\ajuwo\\OneDrive\\Desktop\\Code\\py\\wackamole\\game image files\\brackless holes\\OIP__2_-removebg-preview.png")

        self.create_holes()

    def create_holes(self):
        self.hole1 = self.image.get_rect()
        self.hole1.centerx,self.hole1.centery = self.screen_rect.centerx-55,self.screen_rect.centery-45

        self.hole2 = self.image.get_rect()
        self.hole2.centerx,self.hole2.centery = self.screen_rect.centerx-55,self.screen_rect.centery+25

        self.hole3 = self.image.get_rect()
        self.hole3.centerx,self.hole3.centery = self.screen_rect.centerx-55,self.screen_rect.centery+95

        self.hole4 = self.image.get_rect()
        self.hole4.centerx,self.hole4.centery = self.screen_rect.centerx+15,self.screen_rect.centery-45

        self.hole5 = self.image.get_rect()
        self.hole5.centerx,self.hole5.centery = self.screen_rect.centerx+15,self.screen_rect.centery+25

        self.hole6 = self.image.get_rect()
        self.hole6.centerx,self.hole6.centery = self.screen_rect.centerx+15,self.screen_rect.centery+95

        self.hole7 = self.image.get_rect()
        self.hole7.centerx,self.hole7.centery = self.screen_rect.centerx+85,self.screen_rect.centery-45

        self.hole8 = self.image.get_rect()
        self.hole8.centerx,self.hole8.centery = self.screen_rect.centerx+85,self.screen_rect.centery+25

        self.hole9 = self.image.get_rect()
        self.hole9.centerx,self.hole9.centery = self.screen_rect.centerx+85,self.screen_rect.centery+95

    
    def show_holes(self):
        self.screen.blit(self.image,self.hole1)
        self.screen.blit(self.image,self.hole2)
        self.screen.blit(self.image,self.hole3)
        self.screen.blit(self.image,self.hole4)
        self.screen.blit(self.image,self.hole5)
        self.screen.blit(self.image,self.hole6)
        self.screen.blit(self.image,self.hole7)
        self.screen.blit(self.image,self.hole8)
        self.screen.blit(self.image,self.hole9)
