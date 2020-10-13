import pygame
from pygame.sprite import Sprite
#spirte is built into python as a 2D movable class

class Alien(Sprite):
    '''a class to represent the alien fleet'''

    def __init__(self, ai_game):
        '''initialize alien and set start position'''
        super().__init__()
        self.screen = ai_game.screen

        #load alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #start each new alien near top left screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store alien's exact horizontal position
        self.x = float(self.rect.x)



