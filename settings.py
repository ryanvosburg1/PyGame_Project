class Settings:
    #a class to store all the changing settings

    def __init__(self):
        #initialize game settings
        #screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed = 1.5#ship moves 1.5 pixels

        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3 

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right; -1 means left
        self.fleet_direction = 1