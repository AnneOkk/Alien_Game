class Settings:
    """A class to store all the settings for the game"""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 1200 #create a display window on which we'll draw graphical
        #elements; (1200, 800) defines dimensions -> assigned to self.screen, so it is available = SURFACE
        #each alien etc is its own surface!
        self.screen_height = 800
        self.bg_color = (190, 200, 230) #each color ranges from 0 to 255; (255, 0, 0) is red,
        #(0, 255, 0) is green and (0, 0, 255) is blue; this color is here assigned to self.bg_color
