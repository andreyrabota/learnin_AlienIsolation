import pygame


class Ship():
    """class to manage players ship"""
    def __init__(self, ai_game):
        """sets ship starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #loads ship image and recieves rectang
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        #ship starts at midbuttom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """draws ship in current position"""
        self.screen.blit(self.image, self.rect)
