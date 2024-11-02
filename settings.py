# Creating a class for settings of the game

class Settings:
    # Initializing the game's setting
    def __init__(self):
        self.screen_width = 1600
        self.screen_height = 900
        self.background_color = (135,206,235)
        self.ship_speed = 5

        # Adding bullets specifications

        self.bullet_speed = 2.5
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        