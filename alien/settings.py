class Settings:
    """game settings"""

    def __init__(self):
        """initialise settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (7, 41, 84)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 0.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 200, 200)
        self.bullets_allowed = 5

