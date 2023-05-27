

import pygame,sys
from colors import *
from setting import Settings
from mole import Mole
from mallet import Mallet

pygame.init()
molefile = 'wackamole\\game image files\\backgroundless game images\\mole-removebg-preview.png'
malletfile = 'wackamole\\game image files\\backgroundless game images\\wooden-mallet-vector-9524930-removebg-preview.png'

class Whack_a_mole:

    def __init__(self) -> None:
        #Initialize settings
        self.setting = Settings()

        # Load in the screen
        self.screen = pygame.display.set_mode(self.setting.size)

        # Load in mole object
        self.mole = Mole(molefile,self.setting)

        # Load in ther mallet object
        self.mallet = Mallet(malletfile,self.setting)
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    pygame.mouse.set_visible(False)
                    self.mallet.mallet_rect.x = event.pos[0]
                    self.mallet.mallet_rect.y = event.pos[1]
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mallet.mallet_rect = self.mallet.mallet_rect.inflate(25,-50)

                    if self.mallet.mallet_rect.colliderect(self.mole.mole_rect):
                        self.mole.exclame_status = True

                if event.type == pygame.MOUSEBUTTONUP:
                    self.mallet.mallet_rect = self.mallet.mallet_rect.inflate(-25,50)
                    self.mole.exclame_status = False
                 


            self.update()

    def update(self):
        self.screen.fill(GREEN)
        self.screen.blit(self.mole.mole_image,self.mole.mole_rect)

        if self.mole.exclame_status:
            self.screen.blit(self.mole.exclame,self.mole.exclame_rect)

        self.screen.blit(self.mallet.mallet_image,self.mallet.mallet_rect)
        pygame.display.update()

if __name__ == '__main__':
    new_game = Whack_a_mole()
    new_game.run()