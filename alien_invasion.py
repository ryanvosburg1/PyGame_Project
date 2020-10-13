import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """overall class to manage game assets and behavior."""

    def __init__(self):
        '''initialize the game and create game resources'''
        pygame.init()
        self.settings = Settings()

        '''self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height'''
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        #creates display window and pulls size from settings
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() #pulls bullet
        self.aliens = pygame.sprite.Group()
        self.bg_color = (230,230,230)        #set background color

        self._create_fleet()
    def _create_fleet(self):
        #create fleet of aliens
        #make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width) #space between each alien is 1 alien width

        #determine # of aliens that fit on screen 
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        #create full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
     
    def _create_alien(self,alien_number, row_number): #create alien and place it in row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)#add is like append

    def _check_fleet_edges(self):
        ''''respond if alines reach an edge'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        '''drop entire fleet and change their direction'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1        

    def run_game(self): #run game calls the smaller functions that help it work
        '''start main loop for game'''
        while True: #constantly looping through game
            self._check_events() #checks for keys and processes through checkdown/checkups
            self.ship.update() #updates ship's position each loop through
            self._update_bullets()
            self._update_aliens()
            self._update_screen()#redraws screen each time
            #watch for keyboard and mouse events      
    def _update_bullets(self):           
        self.bullets.update()#updates bullets on screen

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))
            #get rid of bullets that have dissappeared
    def _update_aliens(self):
        '''check if fleet is at edge before update'''
        self._check_fleet_edges()
        '''update positions of all aliens in fleet'''
        self.aliens.update()

    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #if exit window, quit game
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)#goes below to function check keydown
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)  
    def _check_keydown_events(self, event): #respond to keypresses
        if event.key == pygame.K_RIGHT: #move ship to right if arrow right
            self.ship.moving_right = True #gets ship.py settings to move right continuously 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True  
        elif event.key == pygame.K_q:
            sys.exit()  
        elif event.key == pygame.K_SPACE:
            self._fire_bullet() #goes to fire bulet function
    def _check_keyup_events(self, event): #respond to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''create a new bullet and add it to bullets group'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        '''update images on the screen and flip to a new screen'''    
            #redraw screen during each pass trhough loop
        self.screen.fill(self.bg_color)
        self.ship.blitme() #call the ship in front of the background
            #make most recently drawn screen visible
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)#draw puts element by rect attirubte on screen bc screen argument in ()
        pygame.display.flip()

if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game() #in if statement so only runs if called directly