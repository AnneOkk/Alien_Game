class Settings:
    """A class to store all the settings for the game"""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        # create a display window on which we'll draw graphical ship
        self.screen_width = 1200
        self.screen_height = 800
        # (1200, 800) defines dimensions -> assigned to self.screen, so it is available = SURFACE
        # each alien etc is its own surface!
        # self.screen_height = 800

        ## --> screen settings are not needed any longer when we use the FULLSCREEN mode!

        self.bg_color = (190, 200, 230) #each color ranges from 0 to 255; (255, 0, 0) is red,
        #(0, 255, 0) is green and (0, 0, 255) is blue; this color is here assigned to self.bg_color
        self.ship_speed = 4.0 # now when the ship moves, it's position is adjusted by 1.5 pixels rather than 1

        # Bullet settings:
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 26
        self.bullet_color = (190, 0, 0)
        self.bullets_allowed = 10
