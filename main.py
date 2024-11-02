import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
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
        self.bullet = pygame.sprite.Group()
    
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
                    
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_q:
                            exit()
                        elif event.key == pygame.K_SPACE:
                            self._fire_bullet()


                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.ship.moving_left =True
                        
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            self.ship.moving_left = False
            
            def _fire_bullet(self):

                if len(self.bullets) < self.settings.bullets_allowed:
                    new_bullet = Bullet(self)
                    self.bullets.add(new_bullet)            

            def _update_screen():  # Function of drawing screen 
                self.screen.fill(self.setting.background_color)
                
                for bullets in self.bullet.sprites:
                    bullets.draw_bullet()
                
                self.ship.blitme()
                
                pygame.display.flip()
            
            _check_events()
            _update_screen()
            self.ship.update()
            self.clock.tick(60)
            self.bullet.update()

            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

# Making Game instance

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

