import pygame.font
from pygame.sprite import Group

from bot import Bot
from player import Player


class Scores():
    """Вывод игровой информации"""
    def __init__(self,screen,stats, snowball,menu, player, bot_snowball, bot):
        """Подсчет"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.snowball = snowball
        self.menu = menu
        self.player = player
        self.bot_snowball = bot_snowball
        self.bot = bot
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.font_menu = pygame.font.SysFont(None, 24)
        self.key = True
        self.text_color_win = (0,255,128)
        self.font_win = pygame.font.SysFont('comic sans',30 )

        self.image_score()
        self.image_players()



    def image_players(self):
        """Количество жизней"""
        self.players =Group()
        for player_number in range(self.stats.players_left):
            player = Player(self.screen)
            player.rect.x = 15 + player_number * player.rect.width
            player.rect.y = 490
            self.players.add(player)

        self.bots = Group()
        for bots_number in range(self.stats.bots_left):
            bot = Bot(self.screen)
            bot.rect.x = 15 + bots_number * bot.rect.width
            bot.rect.y = 300
            self.bots.add(bot)

    def image_score(self):
        """Рисуем текс в графику"""
        self.score_img = self.font.render("Player life: ", True, self.text_color,(0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.left +150
        self.score_rect.bottom = self.screen_rect.bottom -245

        self.score_imgbot = self.font.render("Bot life: " , True, self.text_color, (0, 0, 0))
        self.score_rectbot = self.score_imgbot.get_rect()
        self.score_rectbot.right = self.screen_rect.left +115
        self.score_rectbot.top = self.screen_rect.top + 265


        self.score_imgmenu = self.font.render("Menu:", True,self.text_color,(0,0,0))
        self.score_rectmenu = self.score_imgmenu.get_rect()
        self.score_rectmenu.right = self.screen_rect.left +100
        self.score_rectmenu.top = self.screen_rect.top + 94

        self.score_imgmenu1 = self.font_menu.render("Нажми 1 что бы играть на время: ", True, self.text_color, (0, 0, 0))
        self.score_rectmenu1 = self.score_imgmenu.get_rect()
        self.score_rectmenu1.right = self.screen_rect.left + 100
        self.score_rectmenu1.top = self.screen_rect.top + 130

        self.score_imgmenu2 = self.font_menu.render("Нажми 2 что бы играть c ограниченным количеством снежков: ", True, self.text_color, (0, 0, 0))
        self.score_rectmenu2 = self.score_imgmenu.get_rect()
        self.score_rectmenu2.right = self.screen_rect.left + 100
        self.score_rectmenu2.top = self.screen_rect.top + 160

        if self.stats.players_left > self.stats.bots_left or self.stats.player_hits > self.stats.bot_hits:
            self.score_playerwin_img = self.font_win.render("Player 1 Win", True, self.text_color_win, (0,0,0))
            self.score_rectplayer_win = self.score_playerwin_img.get_rect()
            self.score_rectplayer_win.left = self.screen_rect.left + 550
            self.score_rectplayer_win.top = self.screen_rect.top + 330
        elif self.stats.players_left < self.stats.bots_left or self.stats.player_hits < self.stats.bot_hits:
            self.score_playerwin_img = self.font_win.render("Player 2 Win", True, self.text_color_win, (0, 0, 0))
            self.score_rectplayer_win = self.score_playerwin_img.get_rect()
            self.score_rectplayer_win.left = self.screen_rect.left + 550
            self.score_rectplayer_win.top = self.screen_rect.top + 330
        else:
            self.score_playerwin_img = self.font_win.render("Ничья", True, self.text_color_win, (0, 0, 0))
            self.score_rectplayer_win = self.score_playerwin_img.get_rect()
            self.score_rectplayer_win.left = self.screen_rect.left + 550
            self.score_rectplayer_win.top = self.screen_rect.top + 330

        self.score_snowballs_left_img = self.font.render("Player snowballs: " + str(self.snowball.col),True, self.text_color, (0,0,0))
        self.score_rect_snowballs_left = self.score_snowballs_left_img.get_rect()
        self.score_rect_snowballs_left.left = self.screen_rect.left + 1000
        self.score_rect_snowballs_left.top = self.screen_rect.top +360

        self.score_time_img =self.font.render(str(self.menu.t), True, self.text_color, (0,0,0,))
        self.score_rect_time = self.score_time_img.get_rect()
        self.score_rect_time.left = self.screen_rect.left +1200
        self.score_rect_time.top = self.screen_rect.top +330

        self.score_bot_snowballs_left_img = self.font.render("Bot snowballs: " + str(self.bot_snowball.col), True, self.text_color, (0, 0, 0))
        self.score_rect_bot_snowballs_left = self.score_bot_snowballs_left_img.get_rect()
        self.score_rect_bot_snowballs_left.left = self.screen_rect.left + 1000
        self.score_rect_bot_snowballs_left.top = self.screen_rect.top + 330

        self.score_playr_hits_img = self.font.render("Player hits: " + str(self.stats.player_hits), True, self.text_color, (0, 0, 0))
        self.score_rect_player_hits = self.score_playr_hits_img.get_rect()
        self.score_rect_player_hits.left = self.screen_rect.left + 15
        self.score_rect_player_hits.top = self.screen_rect.top + 590

        self.score_bots_hits_img = self.font.render("Bot hits: " + str(self.stats.bot_hits), True, self.text_color, (0, 0, 0))
        self.score_rect_bots_hits = self.score_bots_hits_img.get_rect()
        self.score_rect_bots_hits.left = self.screen_rect.left + 15
        self.score_rect_bots_hits.top = self.screen_rect.top + 410
    def show_score(self):
        """Вывод жизней"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.score_imgbot, self.score_rectbot)
        self.players.draw(self.screen)
        self.bots.draw(self.screen)
        if self.player.key == True:
            self.screen.blit(self.score_snowballs_left_img, self.score_rect_snowballs_left)
        if self.bot.key == True:
            self.screen.blit(self.score_bot_snowballs_left_img, self.score_rect_bot_snowballs_left)
        if self.menu.inder == True:
            self.screen.blit(self.score_time_img, self.score_rect_time)
        self.screen.blit(self.score_playr_hits_img, self.score_rect_player_hits)
        self.screen.blit(self.score_bots_hits_img, self.score_rect_bots_hits)
    def show_menu(self):
        if self.key == True:
            self.screen.blit(self.score_imgmenu, self.score_rectmenu)
            self.screen.blit(self.score_imgmenu1, self.score_rectmenu1)
            self.screen.blit(self.score_imgmenu2, self.score_rectmenu2)

    def show_winner(self):
        self.screen.blit(self.score_playerwin_img, self.score_rectplayer_win)
