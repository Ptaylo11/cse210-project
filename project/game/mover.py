import arcade
import random
from game.constants import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, SCALING

img_dict = {
    "grass": "project/game/images/car.png", # there needs to be something here for the game to run.. it will be blank during the game
    "road": "project/game/images/car.png",
    "water": "project/game/images/log.png"
}

class Mover(arcade.Sprite):
    """ Represents the item that moves in a row.
    Can either be one of two types:
    Car - dangerous
    Log - safe

    Stereotype:
        Controller
    
    Attributes:
        type (Str): The type of sprite (road, water, car, etc.)
        center_x (Int): The x-coordinate of the sprite
        center_y (Int): The y-coordinate of the sprite
    """

    def __init__(self, type):
        """ The class constructor.

        Args:
            self (Mover): An instance of Mover
            type (Str): The type of sprite (road, water, car, etc.)
        """

        super().__init__(filename = img_dict[type], scale = SCALING, image_x = 0, image_y = 0, image_width = BLOCK_SIZE * random.randint(2, 4), image_height = BLOCK_SIZE, flipped_horizontally = True)

        self.type = type
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.center_y = SCREEN_HEIGHT - (BLOCK_SIZE / 2)
        if type == "road":
            self.change_x = random.randint(3, 5)
        else:
            self.change_x = random.randint(1, 3)

        if random.randint(0, 1) == 1:
            self.change_x *= -1
            self._set_angle(180)


    def loop(self):
        """ Moves the Mover - called by Director

        Args:
            self (Mover): An instance of Mover
        """

        if self.center_x > SCREEN_WIDTH + self.width:
            self.center_x = 0 - self.width
        elif self.center_x < 0 - self.width:
            self.center_x = SCREEN_WIDTH + self.width

    
    def step_down(self):
        """ Called by the Row class. Moves the sprite's location down one block.

        Args:
            self (Mover): An instance of Mover
        """

        self.center_y -= BLOCK_SIZE