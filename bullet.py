import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """this is for ship bullets"""

    def __init__(self, ai_game):
        """create object at ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create missile in position b (0,0) then ordering correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # missile position
        self.y = float(self.rect.y)

    def update(self):
        # shoot vertically
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        # draws the bullet
        pygame.draw.rect(self.screen, self.color, self.rect)
