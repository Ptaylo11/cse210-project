import arcade
from game.constants import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

class Frog(arcade.Sprite):
    """
    The player controlled character. Inherits from Sprite.

    Stereotype:
        Controller

    Attributes: 
        _starting_x (float): the horizontal position the frog starts at and is reset to
        _starting_y (float): the vertical position the frog starts at and is reset to
        _STATES_LIST (List): a constant list of strings that contains different frog states, used for reference
        _state (String): the Frog's current state, is initialized in reset()
    """

    def __init__(self, img, scaling):
        """
        Class constructor. Calls the super constructor for Sprite-related features.
        Initialized partially in reset().
        
        Args:
            self (Frog): an instance of Frog
            img (String): the filepath to the file used to visually represent Frog
            scaling (Float): used in the super constructor, affects scaling of image
        """
        super().__init__(img, scaling, 0, 0, BLOCK_SIZE, BLOCK_SIZE)
        self._starting_x = BLOCK_SIZE * 8 + (BLOCK_SIZE * .5)
        self._starting_y = BLOCK_SIZE * .5
        self._STATES_LIST = ["NORMAL", "LOG"]
        self._state = None

        self.reset()


    def reset(self):
        """
        Sets the frog's values to default values. Used in initialization
        and whenever the frog dies to reset it.
        
        Args:
            self (Frog): an instance of Frog
        """
        self.center_x = self._starting_x
        self.center_y = self._starting_y
        self.change_x = 0
        self._state = "NORMAL"

    
    def reset_y(self):
        """
        Resets the frog's vertical position to its default value.
        Used when the frog transitions to a new screen.
        
        Args:
            self (Frog): an instance of Frog
        """
        self.center_y = self._starting_y


    def step(self, direction):
        """
        Receives a direction and moves the frog one block
        in the given direction, as well as rotates the image
        to match the direction moved in. After moving, checks
        if the frog is still within the bounds of the screen,
        and if not, moves it back within the screen.
        
        Args:
            self (Frog): an instance of Frog
            direction (String): the direction to be moved in
        """
        if direction == "LEFT":
            self.center_x -= BLOCK_SIZE
            self._set_angle(90)
        elif direction == "RIGHT":
            self.center_x += BLOCK_SIZE
            self._set_angle(-90)
        elif direction == "UP":
            self.center_y += BLOCK_SIZE
            self._set_angle(0)
        elif direction == "DOWN":
            self.center_y -= BLOCK_SIZE
            self._set_angle(180)

        if self.left < 0:
            self.left = 0
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.top <= 0: #This specific line is temporary to keep the frog from going too far off the screen; we can update it later to
                          #account for screen scrolling/generating a new level
            self.top = 0
        if self.bottom <= 0:
            self.bottom = 0

    def set_state(self, new_state="NORMAL"):
        """
        Sets the frog's state to the passed state. If no
        state passed, sets it to the default state of "NORMAL".
        If an invalid state is passed, does not change the
        state and prints an error message to the console. To
        determine an invalid state, it checks if the passed state
        is within the _STATES_LIST constant list.
        
        Args:
            self (Frog): an instance of Frog
            new_state(String): the new state to set Frog to.
        """
        if new_state in self._STATES_LIST:
            self._state = new_state
        else:
            print("Error: Not a valid state")
    
    def get_state(self):
        """
        Returns the frog's current state as a string.
        
        Args:
            self (Frog): an instance of Frog
        """
        return self._state
