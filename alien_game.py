import sys #tools in sys are used to exit the game

import pygame #pygame module contains the functionality we need to make a game

class AlienInvasion:
    """Overall class to manage gane assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init() #initializes the background settings that pygame needs to work properly

        self.screen = pygame.display.set_mode((1200,800)) #create a display window on which we'll draw graphical
        #elements; (1200, 800) defines dimensions -> assigned to self.screen, so it is available 
        pygame.display.set_caption("Alien Invasion")

