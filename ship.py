import pygame


class Ship():
    """class to manage players ship"""
    def __init__(self, ai_game):
        """sets ship starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #loads ship image and recieves rectang
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()
        #ship starts at midbuttom
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        if self.moving_up:
            self.rect.y -= 1
        if self.moving_down:
            self.rect.y += 1

    def blitme(self):
        """draws ship in current position"""
        self.screen.blit(self.image, self.rect)
