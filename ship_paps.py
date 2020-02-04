import pygame

class Ship:
    def __init__(self, ai_game): #ai_game = reference to current instance of the alien invasion class
        """Initialize the ship and set its starting positions"""
        self.screen = ai_game.screen #assign the screen to an attribute of ship, so easy to access in methods in this
        #class
        self.screen_rect = ai_game.screen.get_rect() #access rect attribute and assign it to self.screen_rect -->
        #allows us to place the shop at the correct location on screen

        #Load the ship image and get its rect
        self.image = pygame.transform.scale(pygame.image.load('images/paps.png'), (130, 160))
        #load the image, assign surface returning paps to self.image
        self.rect = self.image.get_rect() #when paps is loaded, we call get_rect()to access the image's surface
        #rect attribute, so we can later use it to place the ship

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw paps at his current location"""
        self.screen.blit(self.image, self.rect) #draws the image to the screen at the position specified by self.rect