import pygame.image


class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        ''' Inicia la config del juego'''
        # Screen settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (100, 100, 255)
        self.bg = pygame.image.load('fondo.jpg')
        self.bg_ajustado = pygame.transform.scale(self.bg, (1920, 1080))
        # ship settings
        """self.ship_speed_factor = 10"""
        self.ship_limit = 3
        # bullet settings
        """self.bullet_speed_factor = 20"""
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = 200, 200, 60
        self.bullet_allowed = 15
        # Alien setting
        """self.alien_speed_factor = 2"""
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = -1
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game."""
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 20
        self.alien_speed_factor = 2
        # Scoring
        self.alien_points = 50


    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)