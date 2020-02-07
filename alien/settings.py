class Settings:
    """game settings"""

    def __init__(self):
        """initialise static settings"""

        # Screen settings
        self.screen_width = 1600
        self.screen_height = 800
        self.bg_color = (7, 41, 84)

        # Ship settings
        self.ship_limit = 1

        # Bullet settings
        self.bullet_width = 450
        self.bullet_height = 15
        self.bullet_color = (100, 200, 150)
        self.bullets_allowed = 50

        # Alien settings
        self.fleet_drop_speed = 50

        # Difficulty factor
        self.speedup_scale = 1.1

        self.initialise_dynamic_settings()

    # noinspection PyAttributeOutsideInit
    def initialise_dynamic_settings(self):
        """Init dynamic settings"""

        self.ship_speed = 3.0
        self.bullet_speed = 5.0
        self.alien_speed = 0.5
        self.alien_points = 50

        # fleet direction 1 is right; -1 is left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points *= self.speedup_scale