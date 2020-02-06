import sys #tools in sys are used to exit the game
import pygame #pygame module contains the functionality we need to make a game
from settings import Settings
from ship_paps import Ship

class AlienInvasion:
    """Overall class to manage gane assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init() #initializes the background settings that pygame needs to work properly
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self) #we make instance of the ship after screen has been created, requires one argument
        #= an instance of AlienInvasion; 'self' refers to current instance of AlienInvasion; this is the parameter that
        #gives Ship access to game's resources, such as the screen object

    def run_game(self): #run_game method controls the game
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color) #here, we fill the screen with the background color (fill()) method acts
            # on surface and takes one argument: a color
            self.ship.blitme() #paps is called to screen, appears on top of background

            #Make most recently drawn screen visible.
            pygame.display.flip() #erases the old screen --> only new screen is visible (can create an illusion of
            #smooth movement (only new positions of game elements shown)

    def _check_events(self):
        # Watch for keyboard and mouse events
        for event in pygame.event.get():  # EVENT = user action --> this for loop = event loop; pygame.event.get()
            # calls a list of events that have taken place since the last time the function was called; any keyboard
            # or mouse event will cause this function to run
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(
            self.settings.bg_color)  # here, we fill the screen with the background color (fill()) method acts
        # on surface and takes one argument: a color
        self.ship.blitme()  # paps is called to screen, appears on top of background

        # Make most recently drawn screen visible.
        pygame.display.flip()  # erases the old screen --> only new screen is visible (can create an illusion of
        # smooth movement (only new positions of game elements shown)

if __name__ == '__main__':
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()


