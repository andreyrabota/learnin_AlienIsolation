import sys
import pygame
from settings import Settings


class AlienIsolation:
    """Class for making resourses and behavior of the game"""

    def __init__(self):
        """initialize a game and set up the game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Isolation")

    def run_game(self):
        """run main cicle of the game"""
        while True:
            #keyboard and mouse capture
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            # showing the screen
            pygame.display.flip()

if __name__ == '__main__':
    # make an instance and start the game
    ai = AlienIsolation()
    ai.run_game()