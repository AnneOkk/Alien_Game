import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set the correct position.
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
                                self.settings.bullet_height) # requires the x- and y-coordinates of the top-left
        # corner rect, and the width and height of the rect
        self.rect.midtop = ai_game.ship.rect.midtop # set the bullet's midtop attribute to match the ship's midtop
        # attribute --> makes it look like the bullet emerges from the top of the ship (like it is fired)

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y) #store decimal values for the bullet's y coordinate, so we can make fine
        # adjustment to the bullet's speed

    def update(self):
        """Move the bullet up the screen"""
        #Uodate the decimal position of the bullet.
        self.y -= self.settings.bullet_speed #when bullet  is fired, it moves up the screen --> decreasing y value
        #Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.ellipse(self.screen, self.color, self.rect)