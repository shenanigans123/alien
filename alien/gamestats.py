class GameStats:
    """Track game statistics"""

    def __init__(self, ai_game):
        """Initialise statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Game state
        self.game_active = True

    def reset_stats(self):
        """Reset stats that can change in the game"""
        self.ships_left = self.settings.ship_limit

