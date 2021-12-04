import arcade
from game.constants import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

class Frog(arcade.Sprite):

    def __init__(self, img, scaling):
        super().__init__(img, scaling, 0, 0, BLOCK_SIZE, BLOCK_SIZE)
        self._starting_x = BLOCK_SIZE * 8 + (BLOCK_SIZE * .5)
        self._starting_y = BLOCK_SIZE * .5
        self._STATES_LIST = ["NORMAL", "LOG", "DEAD"]
        self._state = None

        self.reset()


    def reset(self):
        self.center_x = self._starting_x
        self.center_y = self._starting_y
        self.change_x = 0
        self._state = "NORMAL"

    
    def reset_y(self):
        self.center_y = self._starting_y


    def step(self, direction):
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
        if self.bottom >= SCREEN_HEIGHT:
            self.bottom = SCREEN_HEIGHT

    def die(self):
        """ effectively destroys the frog sprite.
        A new one will only be made when the game is reset.
        """
                            # This is only temporary!!
                            # It will need to change to be able to start over within the program

        self.remove_from_sprite_lists()

    def set_state(self, new_state="NORMAL"):
        if new_state in self._STATES_LIST:
            self._state = new_state
        else:
            print("Error: Not a valid state")
    
    def get_state(self):
        return self._state