import sys #tools in sys are used to exit the game
import pygame #pygame module contains the functionality we need to make a game
from settings import Settings
from ship_paps import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage gane assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init() #initializes the background settings that pygame needs to work properly
        self.settings = Settings()
        self.screen = pygame.display.set_mode([self.settings.screen_width, self.settings.screen_height],
                                              flags = pygame.RESIZABLE)
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self) #we make instance of the ship after screen has been created, requires one argument
        #= an instance of AlienInvasion; 'self' refers to current instance of AlienInvasion; this is the parameter that
        #gives Ship access to game's resources, such as the screen object
        self.bullets = pygame.sprite.Group() # create an instance of the pygame.sprite.Group class
        self.aliens = pygame.sprite.Group() # create an instance of the pygame.sprite.Group class

        self._create_fleet()

    def run_game(self): #run_game method controls the game
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color) #here, we fill the screen with the background color (fill())
            # # method acts on surface and takes one argument: a color
            self.ship.blitme() #paps is called to screen, appears on top of background

            #Make most recently drawn screen visible.
            pygame.display.flip() #erases the old screen --> only new screen is visible (can create an illusion of
            #smooth movement (only new positions of game elements shown)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet position
        self.bullets.update()  # when you call update on a group (in this case, the pygame.sprite.Group), the group
        # automatically calls bullet.update()
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():  # because we cannot remove items from a list in a for loop, we work
            # with a copy of the group (= use the copy() method) to set up the for loop, which allows us to modify
            # bullets inside the loop
            if bullet.rect.bottom <= 0:  # check whether bullet has disappeared over top of screen
                self.bullets.remove(bullet)  # if it has, we remove the bullet
        # print(len(self.bullets)) #insert a print to detect how many bullets currently exist in the game and verify
        # that they're being detected when they reach the top of the screen

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
        if len(self.bullets) < self.settings.bullets_allowed:
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
        self.aliens.draw(self.screen) #to make the alien appear, we need to call the group's draw() method in
        # _update_screen(); when you call .draw() on a group, pygame draws each element of that group in the position
        # defined in rect attribute; the draw method only requires one argument: the surface on which to draw the
        # elements from group

        # Make most recently drawn screen visible.
        pygame.display.flip()  # erases the old screen --> only new screen is visible (can create an illusion of
        # smooth movement (only new positions of game elements shown)

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Make one alien and find the numbers of aliens in a row
        # Spacing between aliens is equal to one alien width
        alien = Alien(self) # we first create an alien, so we can know its width and height to place the other
        # aliens (this alien is not part of the fleet, but just taken as exampele)
        alien_width, alien_height = alien.rect.size

        # get the alien's width and height from its rect attribute
        available_space_x = self.settings.screen_width - (2 * alien_width) #calculate space that is available for all
        # aliens
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of aliens that fit on the screen
        ship_height = self.ship.rect.height # get the ship height from its rect attribute
        available_space_y = (self.settings.screen_height -
                             (alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row_number in range (number_rows):
            for alien_number in range(number_aliens_x): # loop that counts from 0 to number of aliens we need to make
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + alien.rect.height * row_number
        self.aliens.add(alien)

if __name__ == '__main__':
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()


