import random

import pygame
import sys

from BotSnowball import Botsnowball
from snowball import Snowball


def events(screen, stats, sc, menu, player, snowballs, bot, bot_snowballs, snowball, bot_snowball):
    """Обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.mright = True

            elif event.key == pygame.K_LEFT:
                player.mleft = True

            elif event.key == pygame.K_SPACE:
                if snowball.col != 0 and player.key == True:
                    new_snowball = Snowball(screen, player)
                    snowballs.add(new_snowball)
                    snowball.col -= 1
                    print(snowball.col)
                    sc.show_score()
                    sc.image_score()
                elif not player.key:
                    new_snowball = Snowball(screen, player)
                    snowballs.add(new_snowball)

            if event.key == pygame.K_1:
                menu.inder = True
                player.create_gun()
                # menu.show_time()
                snowballs.empty()
                bot_snowballs.empty()
                stats.bots_left = 3
                stats.players_left = 3
                sc.image_players()
                sc.key = False
                sc.show_score()
                stats.bot_hits = 0
                stats.player_hits = 0
                # menu.timer =
                # menu.image_time()

            elif event.key == pygame.K_2:
                player.key = True
                bot.key = True
                player.create_gun()
                snowballs.empty()
                bot_snowballs.empty()
                stats.bots_left = 3
                stats.players_left = 3
                sc.show_score()
                sc.image_score()
                sc.key = False
                stats.bot_hits = 0
                stats.player_hits = 0
                sc.image_players()


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.mright = False

            elif event.key == pygame.K_LEFT:
                player.mleft = False

        i = random.randint(1, 5)
        # print(i)
        if i == 3:
            if len(bot_snowballs) < 3 and bot.sleep == False:
                if bot_snowball.col != 0 and bot.key == True:
                    new_botsnowball = Botsnowball(screen, bot)
                    bot_snowballs.add(new_botsnowball)
                    bot_snowball.col -= 1
                    print(bot_snowball.col)
                elif not bot.key:
                    new_botsnowball = Botsnowball(screen, bot)
                    bot_snowballs.add(new_botsnowball)


def update_bot(bot):
    bot.update_bot()


def update(bg_color, screen, stats, sc, menu, player, snowballs, bot, bot_snowballs, snowball, bot_snowball):
    """обновление экрана"""
    screen.fill(bg_color)
    sc.show_score()
    sc.show_menu()
    sc.image_score()
    # menu.show_time()

    if menu.t == 0:
        if stats.players_left != 0 and stats.bots_left != 0:
            if stats.player_hits > stats.bot_hits:
                sc.show_winner()
                sc.show_score()
            elif stats.player_hits < stats.bot_hits:
                sc.show_winner()
                sc.show_score()
            else:
                sc.show_winner()
                sc.show_score()
        elif stats.players_left > stats.bots_left:
            sc.show_winner()
            sc.show_score()
        elif stats.players_left < stats.bots_left:
            sc.show_winner()
            sc.show_score()
        else:
            sc.show_winner()
            sc.show_score()

        stats.run_game = False

    if snowball.col == 0 and bot_snowball.col == 0:
        if len(snowballs) == 0 and len(bot_snowballs) == 0:
            if stats.players_left != 0 and stats.bots_left != 0:
                if stats.player_hits > stats.bot_hits:
                    sc.show_winner()
                    sc.show_score()
                elif stats.player_hits < stats.bot_hits:
                    sc.show_winner()
                    sc.show_score()
                else:
                    sc.show_winner()
                    sc.show_score()
            elif stats.players_left > stats.bots_left:
                sc.show_winner()
                sc.show_score()
            elif stats.players_left > stats.bots_left:
                sc.show_winner()
                sc.show_score()
            else:
                sc.show_winner()
                sc.show_score()

            stats.run_game = False

    if stats.players_left > stats.bots_left == 0:
        sc.show_winner()
        stats.run_game = False
    elif stats.players_left < stats.bots_left and stats.players_left == 0:
        sc.show_winner()
        stats.run_game = False

    for snowball in snowballs.sprites():
        snowball.draw_snowball()

    for bot_snowball in bot_snowballs.sprites():
        bot_snowball.draw_botsnowball()
    player.output()
    bot.output_bot()
    pygame.display.flip()


def update_snowballs(stats, sc, bot, snowballs, bot_snowballs):
    """Обновление позиции снежков"""

    if stats.bots_left > 0:
        snowballs.update()
        for snowball in snowballs.copy():
            if snowball.rect.bottom <= 0:
                snowballs.remove(snowball)
        if pygame.sprite.spritecollideany(bot, snowballs):
            bot_kill(stats, bot, sc, snowballs, bot_snowballs)
            sc.image_players()

    else:
        stats.run_game = False


def update_bot_snowballs(player, sc, bot_snowballs, stats, snowballs):
    """Обновление позиции снежков бота"""
    if stats.players_left > 0:
        bot_snowballs.update()
        for bot_snowball in bot_snowballs.copy():
            if bot_snowball.rect.top >= 800:
                bot_snowballs.remove(bot_snowball)
        # print(len(bot_snowballs))
        if pygame.sprite.spritecollideany(player, bot_snowballs):
            player_kill(stats, player, sc, bot_snowballs, snowballs)
            sc.image_players()

    else:
        stats.run_game = False


def bot_kill(stats, bot, sc, snowballs, bot_snowballs):
    """Попадание по врагу"""
    stats.bots_left -= 1
    snowballs.empty()
    sc.image_players()
    bot_snowballs.empty()
    # time.sleep(1)
    print(stats.bots_left)
    sc.image_score()
    bot.sleep = True
    if stats.players_left < 3:
        stats.players_left += 1
    stats.player_hits += 1
    print("Попадания: " + str(stats.player_hits))
    sc.show_score()


def player_kill(stats, player, sc, bot_snowballs, snowballs):
    """По падение по игроку"""
    stats.players_left -= 1
    bot_snowballs.empty()
    sc.image_players()
    snowballs.empty()
    # time.sleep(1)
    print(stats.players_left)
    sc.image_score()
    player.sleep = True
    if stats.bots_left < 3:
        stats.bots_left += 1
    stats.bot_hits += 1


def stop_game(player, bot, snowballs, bot_snowballs):
    player.sleep = True
    bot.sleep = True
    snowballs.empty()
    bot_snowballs.empty()
