import sys
import pygame


class AlienIsolation:
    """Class for making resourses and behavior of the game"""

    def __init__(self):
        """initialize a game and set up the game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Isolation")

    def run_game(self):
        """run main cicle of the game"""
        while True:
            #keyboard and mouse capture
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # showing the screen
            pygame.display.flip()

if '__name__' == '__main__':
    # make an instance and start the game
    ai = AlienIsolation()
    ai.run_game()