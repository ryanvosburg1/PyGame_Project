import pygame

class Ship:
    '''a class to manage the ship'''

    def __init__(self, ai_game):
        '''initialize ship and set its start position'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() #to use ships rectangle attribute
        #start each new hip at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #pygame lets you treat all elements like rectangles
    def blitme(self):
        #draw the ship at current spot
        self.screen.blit(self.image, self.rect)

        