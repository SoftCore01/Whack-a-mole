import pygame
import time
from colors import *

class Timer:

    def __init__(self,game,n) -> None:
        self.time = n
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = game.setting

        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        self.countdown()


    def countdown(self):
        while self.time:
            mins, secs = divmod(self.time,60)
            timer = '{:02d}:{:02d}'.format(mins,secs)
            self.timer_image = self.font.render(timer,True,self.text_color,self.setting.bg_color)
            #print(timer,end="\r")
            self.timer_rect = self.timer_image.get_rect()
            self.timer_rect.x,self.timer_rect.y = 0,0
            time.sleep(1)
            self.time -=1

    def show_timer(self):
        self.screen.blit(self.timer_image,self.timer_rect)

