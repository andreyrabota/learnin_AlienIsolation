import pygame


class Ship():
    """class to manage players ship"""
    def __init__(self, ai_game):
        """sets ship starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # loads ship image and recieves rectang
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()

        # ship starts at midbuttom
        self.x = float(self.rect.x)
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.x > 0:
            self.rect.x -= self.settings.ship_speed
        if self.moving_up and self.rect.y > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed

    def blitme(self):
        """draws ship in current position"""
        self.screen.blit(self.image, self.rect)
