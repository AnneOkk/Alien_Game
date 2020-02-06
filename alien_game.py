import sys #tools in sys are used to exit the game
import pygame #pygame module contains the functionality we need to make a game
from settings import Settings
from ship_paps import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage gane assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init() #initializes the background settings that pygame needs to work properly
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self) #we make instance of the ship after screen has been created, requires one argument
        #= an instance of AlienInvasion; 'self' refers to current instance of AlienInvasion; this is the parameter that
        #gives Ship access to game's resources, such as the screen object
        self.bullets = pygame.sprite.Group() # create an instance of the pygame.sprite.Group class

    def run_game(self): #run_game method controls the game
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update() # when you call update on a group (in this case, the pygame.sprite.Group), the group
            # automatically calls bullet.update()
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
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        new_bullet = Bullet(self) #make an instance of Bullet and call it new_bullet
        self.bullets.add(new_bullet) #add the new instance to the group bullets (add() is similar to append(), but it's
        # a method that was written for Pygame groups

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(
            self.settings.bg_color)  # here, we fill the screen with the background color (fill()) method acts
        # on surface and takes one argument: a color
        self.ship.blitme()  # paps is called to screen, appears on top of background
        for bullet in self.bullets.sprites(): #bullet.sprites method returns a list of all sprites in the group bullets
            bullet.draw_bullet() #To draw all fired bullets to the screen, we loop through the sprites in bullets
            # and call draw_bullet() on each one

        # Make most recently drawn screen visible.
        pygame.display.flip()  # erases the old screen --> only new screen is visible (can create an illusion of
        # smooth movement (only new positions of game elements shown)

if __name__ == '__main__':
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()


