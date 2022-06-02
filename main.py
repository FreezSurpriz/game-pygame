import pygame,controls
import  sys


import schedule
from stats import Stats
from player import Player
from pygame.sprite import Group
from bot import Bot
from  scores import Scores
from menu import Menu
from snowball import Snowball
from BotSnowball import Botsnowball


def run():

    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("Снежки")
    bg_color = (0, 0, 0)
    player = Player(screen)
    bot = Bot(screen)
    bot_snowball = Botsnowball(screen, bot)
    snowballs = Group()

    bot_snowballs = Group()
    stats = Stats()
    snowball = Snowball(screen, player)
    menu = Menu(screen, stats)
    sc = Scores(screen, stats, snowball, menu, player, bot_snowball,bot)



    while True:
        controls.events(screen,stats,sc,menu, player, snowballs,bot, bot_snowballs,snowball, bot_snowball)
        menu.timegame()

        if stats.run_game:
            player.update_player()
            controls.update_bot(bot)
            bot_snowballs.update()
            controls.update(bg_color, screen, stats, sc,menu, player, snowballs,bot,bot_snowballs, snowball, bot_snowball)
            controls.update_snowballs(stats, sc,  bot, snowballs, bot_snowballs)
            schedule.run_pending()
            controls.update_bot_snowballs(player, sc, bot_snowballs,stats,snowballs)
            ##controls.time_end(menu,stats,sc, screen)



run()