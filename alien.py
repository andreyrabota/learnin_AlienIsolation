import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """this class provides one alien ship"""

    def __init__(self, ai_game):
        """initialize an alien and set his position"""
        super().__init__()
        self.screen = ai_game.screen

        # load alien image
        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()

        # each aslien starts at nw corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save horizontal position
        self.x = float(self.rect.x)
