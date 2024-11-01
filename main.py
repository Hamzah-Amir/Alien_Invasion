import sys
import pygame
from settings import Settings
from ship import Ship
pygame.init()

# Creating a class to manage display and basic things

class AlienInvasion:

    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("ALien Invasion")
        self.ship = Ship(self)
    
    def run_game(self):
            
        while True:
            
            # Function for handling events in game
            
            def _check_events():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                     
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            self.ship.moving_right = True

                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            self.ship.moving_right = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.ship.moving_left =True
                        
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            self.ship.moving_left = False
                        

            def _update_screen():  # Function of drawing screen 
                self.screen.fill(self.setting.background_color)
                self.ship.blitme()
                
                pygame.display.flip()
            
            _check_events()
            _update_screen()
            self.ship.update()
            self.clock.tick(60)

# Making Game instance

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

