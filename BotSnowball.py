import pygame
class Botsnowball(pygame.sprite.Sprite):

    def __init__(self,screen,bot):
        """Создаем снежок в позиции врага"""
        super(Botsnowball, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 5)
        self.color = 255, 255, 255
        self.speed = 1
        self.col = 10
        self.rect.centerx = bot.rect.centerx
        self.rect.top = bot.rect.bottom
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение снежка вниз"""
        self.y += self.speed
        self.rect.y = self.y

    def draw_botsnowball(self):
        """рисуем снежок """
        pygame.draw.rect(self.screen, self.color, self.rect)



