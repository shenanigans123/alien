class GameStats:
    """Track game statistics"""

    def __init__(self, ai_game):
        """Initialise statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

        # Game state
        self.game_active = False

        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Reset stats that can change in the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1