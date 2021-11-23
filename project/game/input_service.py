from game import constants
import arcade
from arcade import Window

class InputService(Window):
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider
    """
    def __init__(self):
        super().__init__()

    def on_key_press(self, frog, symbol = None, modifier = None):
        """Handle user key input.
        
        Args:
            symbol (int): the key that was pressed.
            frog (Sprite): the frog sprite.
        """
        if symbol == arcade.key.W:
            frog.change_y = constants.BLOCK_SIZE

        if symbol == arcade.key.S:
            frog.change_y = constants.BLOCK_SIZE * -1

        if symbol == arcade.key.A:
            frog.change_x = constants.BLOCK_SIZE * -1

        if symbol == arcade.key.D:
            frog.change_x = constants.BLOCK_SIZE