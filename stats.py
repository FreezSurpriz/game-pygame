class Stats:
    """Отслеживание статистики"""

    def __init__(self):
        """Инициализация статистики"""
        self.player_hits = None
        self.bot_hits = None
        self.players_left = None
        self.bots_left = None
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        """Статистика изменяющийся во время игры"""
        self.bots_left = 3
        self.players_left = 3
        self.bot_hits = 0
        self.player_hits = 0
