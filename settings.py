class Settings:
    #a class to store all the changing settings

    def __init__(self):
        #initialize game settings
        #screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed = 1.5#ship moves 1.5 pixels