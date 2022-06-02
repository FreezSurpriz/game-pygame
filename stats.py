class Stats():
    """Отслеживание статистики"""
    def __init__(self):
        """Инициализация статистики"""
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        """Статистика изменяющийся во время игры"""
        self.bots_left = 3
        self.players_left = 3
        self.bot_hits = 0
        self.player_hits = 0