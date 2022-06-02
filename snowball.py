import  pygame

class Snowball(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        """Создаем снежок"""
        super(Snowball, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 5)
        self.color = 255, 255, 255
        self.speed = 1
        self.col = 10
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение снежка вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_snowball(self):
        """Рисуем снежок на экране"""
        pygame.draw.rect(self.screen,self.color, self.rect)
