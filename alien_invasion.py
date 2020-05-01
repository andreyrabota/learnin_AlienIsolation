import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienIsolation:
    """Class for making resourses and behavior of the game"""

    def __init__(self):
        """initialize a game and set up the game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Isolation")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """run main cicle of the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _check_events(self):
        # keyboard and mouse capture
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.ship.moving_right = True
                elif event.key == pygame.K_a:
                    self.ship.moving_left = True
                elif event.key == pygame.K_w:
                    self.ship.moving_up = True
                elif event.key == pygame.K_s:
                    self.ship.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self.fire_bullet()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.ship.moving_right = False
                elif event.key == pygame.K_a:
                    self.ship.moving_left = False
                elif event.key == pygame.K_w:
                    self.ship.moving_up = False
                elif event.key == pygame.K_s:
                    self.ship.moving_down = False
    def fire_bullet(self):
        #create new bullet and set it to bullet group
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _update_screen(self):
        """update images on screen and renews the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
if __name__ == '__main__':
    # make an instance and start the game
    ai = AlienIsolation()
    ai.run_game()