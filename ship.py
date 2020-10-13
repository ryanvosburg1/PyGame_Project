import pygame

class Ship:
    '''a class to manage the ship'''

    def __init__(self, ai_game):
        '''initialize ship and set its start position'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() #to use ships rectangle attribute
        #start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #pygame lets you treat all elements like rectangles

        #store a decimal value for ship' horizontal position
        self.x = float(self.rect.x)

        #movement 
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update ships positions based on movement flas
        #update ship's x value not rectangle
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        #update rect object from self.x
        self.rect.x = self.x
    def blitme(self):
        #draw the ship at current spot
        self.screen.blit(self.image, self.rect)

        