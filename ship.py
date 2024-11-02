import pygame
pygame.init()

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.setting
        # self.ship_speec = 2

        # Loading ship image

        self.image = pygame.image.load("redfighter0005.png")
        self.rect = self.image.get_rect()

        # Setting starting point of the ship at bottom centre
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # Enabling continous motion of ship

        self.moving_right = False  
        self.moving_left = False  

    def update(self):
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        
        if self.moving_left and self.rect.left > 0:  
            self.x -= self.setting.ship_speed
        
        self.rect.x = self.x
        

    def blitme(self):
        self.screen.blit(self.image, self.rect)