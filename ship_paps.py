import pygame

class Ship:
    def __init__(self, ai_game): #ai_game = reference to current instance of the alien invasion class
        """Initialize the ship and set its starting positions"""

        self.screen = ai_game.screen #assign the screen to an attribute of ship, so easy to access its methods in this
        #class

        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect() #access rect attribute and assign it to self.screen_rect -->
        #allows us to place the shop at the correct location on screen

        #Load the ship image and get its rect
        self.image = pygame.transform.scale(pygame.image.load('images/paps.png'), (120, 190))

        #load the image, assign surface returning paps to self.image
        self.rect = self.image.get_rect() #when paps is loaded, we call get_rect()to access the image's surface
        #rect attribute, so we can later use it to place the ship

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False

        self.moving_left = False

        self.moving_up = False

        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        #Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        #Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw paps at his current location"""
        self.screen.blit(self.image, self.rect) #draws the image to the screen at the position specified by self.rect
