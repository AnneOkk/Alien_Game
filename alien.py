import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien/ attacking instance"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting point"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the attacker image and get its rect
        self.image = pygame.transform.scale(pygame.image.load('images/windbeutel.png'), (100, 90))
        # load the image, assign surface returning paps to self.image
        self.rect = self.image.get_rect()  # when paps is loaded, we call get_rect()to access the image's surface
        # rect attribute, so we can later use it to place the attacker
        # Store a decimal value for the attacker's horizontal position
        self.rect.x = self.rect.width # add space to the left of the attacker, that is equal to attacker width 
        self.rect.y = self.rect.height # add space above the attacker that is equal to attacker height 

        # Store the exact horizontal position
        self.x = float(self.rect.x) # we're mainly concerned with horizontal speed, so we track this precisely 
        # (using floating point) 
