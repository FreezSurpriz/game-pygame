import pygame
from threading import Timer
import time
global sendEnmy
class Menu():
    def __init__(self,screen, stats):

        self.inder = False
        self.timesleft = 10
        self.screen = screen
        self.stats = stats
        self.timer = 20
        self.t = 1
        self.screen_rect = screen.get_rect()
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 36)
        self.knopka = True
        self.timegame()

        #self.image_time()

    def timegame(self):
        ##razniza = self.timer + pygame.time.get_ticks()
        if self.inder == True and self.t > 0:
            if pygame.time.get_ticks() != 0 and self.knopka == True :
                self.timer = (self.timer + pygame.time.get_ticks()/1000)+1
                self.knopka = False
            self.t =  int((self.timer - pygame.time.get_ticks()/1000))

            ##print(self.t)



    #def image_time(self):










