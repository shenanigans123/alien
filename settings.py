class Settings:
    """game settings"""

    def __init__(self):
        """initialise settings"""

        # Screen settings
        self.screen_width = 1600
        self.screen_height = 800
        self.bg_color = (7, 41, 84)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 0.6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 200, 200)
        self.bullets_allowed = 50

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction 1 is right; -1 is left
        self.fleet_direction = 1