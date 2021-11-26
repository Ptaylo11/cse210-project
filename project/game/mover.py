import arcade
import random
from game.constants import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, SCALING

img_dict = {
    "grass": "",
    "road": "project/game/images/car.png",
    "water": "project/game/images/log.png"
}

class Mover(arcade.Sprite):
    """ Represents the item that moves in a row.
    Can either be one of two types:
    Car - dangerous
    Log - safe
    """

    def __init__(self, type):
        """ The class constructor.
        """

        super().__init__(img_dict[type], SCALING, 0, 0, BLOCK_SIZE * random.randint(2, 4), BLOCK_SIZE)

        self.type = type
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.center_y = SCREEN_HEIGHT - (BLOCK_SIZE / 2)
        self.change_x = random.randint(3, 5)


    def loop(self):
        """ moves the mover - called by director
        """

        if self.center_x > SCREEN_WIDTH + self.width:
            self.center_x = 0 - self.width
        elif self.center_x < 0 - self.width:
            self.center_x = SCREEN_WIDTH + self.width

    
    def step_down(self):
        """ Called by the Row class. Moves the sprite's location down one block.
        """

        self.center_y -= BLOCK_SIZE