import arcade
from game.constants import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, SCALING

img_dict = {
    "grass": "project/game/images/grass.png",
    "road": "project/game/images/road.png",
    "water": "project/game/images/water.png"
}

class Background(arcade.Sprite):
    """ The background populated behind each row in the game.
    Can either be:
    grass - safe
    road - safe
    water - dangerous
    """

    def __init__(self, type):
        """The class constructor.
        
        Args:
            self (Background): an instance of Background.
            type (Image): which of the three background images is being used
        """
        super().__init__(img_dict[type], SCALING)

        self.type = type
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT - (BLOCK_SIZE / 2)
        self.width = SCREEN_WIDTH
        self.height = BLOCK_SIZE
    

    def step_down(self):
        """ Moves the entire background sprite down one block.
        Called by the Row class.
        """

        self.center_y -= BLOCK_SIZE