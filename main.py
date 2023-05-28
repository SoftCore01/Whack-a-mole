

import json
import pygame,sys
from colors import *
from hole import Hole
from mole import Mole
from time import sleep
from mallet import Mallet
from buttons import Button
from exclame import Exclame
from setting import Settings
from gamestats import GameStats
from score_board import Scoreboard


pygame.init()

class Whack_a_mole:
    def __init__(self) -> None:
        #Initialize settings
        self.setting = Settings()

        # Load in the screen
        self.screen = pygame.display.set_mode(self.setting.size)
        self.screen_rect = self.screen.get_rect()


        # Load in mole object
        self.mole_group = pygame.sprite.Group()

        # Load mole holes
        self.hole = Hole(self)

        # Load in the mallet object
        self.mallet = Mallet(self)

        # Load in the exclame object
        self.exclame = Exclame(self)

        # Load the stats class
        self.stats = GameStats(self)

        # Load the scoreboard
        self.sb = Scoreboard(self)

        # Initialize font style
        self.font = pygame.font.SysFont('Consolas',30)

        # Game state variables
        self.play = False
        self.paused = False
        self.end = False

        # Game buttons
        self.start_img = pygame.image.load('wackamole\\menu screen images\\start_btn.png')
        self.exit_img = pygame.image.load('wackamole\\menu screen images\\exit_btn.png')
        self.quit_img = pygame.image.load('wackamole\\menu screen images\\button_quit.png')
        self.resume_img = pygame.image.load('wackamole\\menu screen images\\button_resume.png')
        self.restart_img = pygame.image.load('wackamole\\menu screen images\\restart.png')
        self.load_buttons()




        # Time format
        self.mins,self.secs = divmod(self.setting.game_time,60)
        self.text = "{:02d}:{:02d}".format(self.mins,self.secs)

        self.fps = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT,1000)
        

    def run(self):
#        if self.paused:
#            self.load_buttons()
#        else:
            while True:
                self._check_events()

                if self.play and not self.paused:
                    if len(self.mole_group) < 3:
                        self.mole_appear()
                # The event controlling the timer

                self.mole_group.update()
                self.update()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.pause(event)
            elif event.type == pygame.USEREVENT and self.play and not self.paused:
                self.countdown()
                if self.setting.game_time == 0:
                    self.restart()
            elif event.type == pygame.MOUSEMOTION:
                self.mousepos(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_exit_button(mouse_pos)
                self._check_resume_button(mouse_pos)
                self._check_restart_button(mouse_pos)
                self._check_quit_button(mouse_pos)
                self.mousedown()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouseup()


    def _check_play_button(self,mousepos):
        button_clicked = self.start_button.rect.collidepoint(mousepos)
        if button_clicked and not self.play:
            self.stats.reset_stat()
            self.play = True

    def _check_exit_button(self,mousepos):
        button_clicked = self.exit_button.rect.collidepoint(mousepos)
        if button_clicked and not self.play:
            sys.exit()

    def _check_resume_button(self,mousepos):
        button_clicked = self.resume_button.rect.collidepoint(mousepos)
        if button_clicked and not self.play:
            #print('resume')
            self.play = True
            self.paused = False      

    def _check_restart_button(self,mousepos):
        button_clicked = self.restart_button.rect.collidepoint(mousepos)
        if button_clicked and not self.play:
            #self.stats.reset_stat()
            self.play = True
            self.paused = False
            self.stats.score = 0
            self.setting.game_time = self.setting.initial_game_time+1
        

    def _check_quit_button(self,mousepos):
        button_clicked = self.quit_button.rect.collidepoint(mousepos)
        if button_clicked and not self.play:
            sys.exit()

    def pause(self,event):
        if event.key == pygame.K_ESCAPE:
            pygame.mouse.set_visible(True)
            self.mole_group.empty()
            self.paused = True
            self.play = False
            #print(self.paused)

    def restart(self):
        if self.setting.game_time == 0:
            pygame.mouse.set_visible(True)
            self.mole_group.empty()
            self.paused = True 
            self.play = False
            self.end = True
            


    def countdown(self):
        self.setting.game_time -= 1
        self.mins,self.secs = divmod(self.setting.game_time,60)
        self.text = "{:02d}:{:02d}".format(self.mins,self.secs) if self.setting.game_time > 0 else 'Game Over'
        if self.setting.game_time == 0:
            with open(self.stats.hs_file,'w') as f:
                json.dump(self.stats.high_score,f)
            pass

        
    def mousepos(self,event):
        if self.play:
            pygame.mouse.set_visible(False)
            self.mallet.rect.x = event.pos[0]
            self.mallet.rect.y = event.pos[1]


    def mousedown(self):
        self.mallet.rect = self.mallet.rect.inflate(25,-50)
        #if pygame.sprite.spritecollide(self.mallet,self.mole,True):
        #    self.mole.exclame_status = True
        for mole in self.mole_group.sprites():
            if self.mallet.rect.colliderect(mole.rect):
                self.mole_group.remove(mole)
                self.exclame.rect.x = mole.rect.x-60
                self.exclame.rect.y = mole.rect.y-50
                self.exclame.status = True
                self.stats.score += self.setting.mole_point
                self.sb.prep_score()
                self.sb.check_high_score()


    def mouseup(self):
        self.mallet.rect = self.mallet.rect.inflate(-25,50)
        self.exclame.status = False


    def mole_appear(self):
        self.mole = Mole(self,self.mole_group)
        self.mole.time = pygame.time.get_ticks()

    def game_restart(self):
        self.setting.game_time = self.setting.initial_game_time+1
        self.stats.reset_stat()


    def load_buttons(self):
        self.start_button = Button(
            self,self.screen_rect.centerx,self.screen_rect.centery-50,
            self.start_img,0.5
        )
        self.exit_button = Button(
            self,self.screen_rect.centerx,self.screen_rect.centery+50,
            self.exit_img,0.5
        ) 
        self.quit_button = Button(
            self,self.screen_rect.centerx,self.screen_rect.centery+100,
            self.quit_img,0.5
        ) 
        self.resume_button =Button(
            self,self.screen_rect.centerx,self.screen_rect.centery-100,
            self.resume_img,0.5
        ) 
        self.restart_button = Button(
            self,self.screen_rect.centerx,self.screen_rect.centery,
            self.restart_img,0.5
        ) 



    def update(self):
        self.screen.fill(self.setting.bg_color)
        self.hole.show_holes()
        if not self.play and not self.paused:
            self.start_button.draw()
            self.exit_button.draw()

        if self.end and self.paused:
            self.restart_button.draw()
            self.quit_button.draw()

        if self.paused and not self.end :
            self.resume_button.draw()
            self.restart_button.draw()
            self.quit_button.draw()

        for mole in self.mole_group.sprites():
            self.screen.blit(mole.image,mole.rect)
            self.exclame.display()

        self.sb.show_score()
        if self.play and not self.paused:
            self.screen.blit(self.mallet.image,self.mallet.rect)
        self.screen.blit(self.font.render(self.text,True,(0,0,0)),(32,48))

        pygame.display.update()
        self.fps.tick(25)
        

if __name__ == '__main__':
    new_game = Whack_a_mole()
    new_game.run()