import pygame
pygame.init()

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loading ship image

        self.image = pygame.image.load("redfighter0005.png")
        self.rect = self.image.get_rect()

        # Setting starting point of the ship at bottom centre
        self.rect.midbottom = self.screen_rect.midbottom

        # Enabling continous motion of ship

        self.moving_right = False  
        self.moving_left = False  

    def update(self):
        if self.moving_right:
            self.rect.x +=1.5
        elif self.moving_left:
            self.rect.x -=2.5

    def blitme(self):
        self.screen.blit(self.image, self.rect)