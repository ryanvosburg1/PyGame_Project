import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """overall class to manage game assets and behavior."""

    def __init__(self):
        '''initialize the game and create game resources'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        #creates display window and pulls size from settings
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        #set background color
        self.bg_color = (230,230,230)

    def run_game(self): #run game calls the smaller functions that help it work
        '''start main loop for game'''
        while True:
            self._check_events()
            self.ship.update() #updates ship's position each loop through
            self._update_screen()
            #watch for keyboard and mouse events
    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #if exit window, quit game
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT: #move ship to right if arrow right
                        self.ship.moving_right = True #gets ship.py settings to move right continuously 
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
    def _update_screen(self):
        '''update images on the screen and flip to a new screen'''    
            #redraw screen during each pass trhough loop
        self.screen.fill(self.bg_color)
        self.ship.blitme() #call the ship in front of the background
            #make most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game() #in if statement so only runs if called directly