class Settings:
    #a class to store all the changing settings

    def __init__(self):
        #initialize game's static settings
        #screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed = 1.5#ship moves 1.5 pixels right now
        self.ship_limit = 3 #how many lives

        #bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3 

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right; -1 means left
        self.fleet_direction = 1

        #how quickly game speeds up at each level
        self.speedup_scale = 1.1

        #how quickly alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''initialize settings that change throughout game at dif levels'''
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #fleet_drection of 1 is right, -1 is left
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50

    #to increase speed at each new level and alien pts value
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
