import  pygame
import time
from threading import Timer
from pygame.sprite import Sprite
class Player(Sprite):
    def __init__(self, screen):
        """Инициализация игрока"""
        super(Player, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/pngwing.com.png')
        self.rect = self.image.get_rect()
        self.scree_rect = screen.get_rect()
        self.rect.centerx = self.scree_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.scree_rect.bottom
        self.mright = False
        self.mleft = False
        self.sleep = False
        self.key = False

    def output(self):
        """Рисование игрока"""
        self.screen.blit(self.image, self.rect)


    def update_player(self):
        """Обновление позиции игрока"""
        def sleep():
            self.sleep = False
        if self.sleep == False:
            if self.mright and self.rect.right < self.scree_rect.right:
                self.center +=0.7
            if self.mleft and self.rect.left > 0:
                self.center -=0.7
            self.rect.centerx = self.center
        else:
            t = Timer(3,sleep)
            t.start()

    def create_gun(self):
        self.center = self.scree_rect.centerx

        # self.score_img = self.font.render("Player life: ", True, self.text_color, (0, 0, 0))
        # self.score_rect = self.score_img.get_rect()
        # self.score_rect.right = self.screen_rect.left + 150
        # self.score_rect.bottom = self.screen_rect.bottom - 285