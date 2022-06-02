import pygame
import  schedule
from threading import Timer
from pygame.sprite import Sprite
class Bot(Sprite):
    def __init__(self, screen):
        """Инициализация бота"""
        super(Bot, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/bot.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.top = self.screen_rect.top
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.a = True
        self.sleep = False
        self.key = False

    def output_bot(self):
        """Отрисовка бота """
        self.screen.blit(self.image, self.rect)

    def update_bot(self):
        """Движение бота"""
        ##print(self.a)
        ##print(self.x)
        def sleep():
            self.sleep = False
        if self.sleep == False:
            if self.rect.right == self.screen_rect.right:
                self.a = False
            elif self.rect.x < 1280 and self.a == True:
                self.x += 0.1
                self.rect.x = self.x
            if self.rect.left == 0:
                self.a = True
            elif self.rect.left > 0 and self.a == False:
                self.x -=  0.1
                self.rect.x = self.x
        else:
            t = Timer(3.0, sleep)
            t.start()














