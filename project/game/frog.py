import arcade
from game.constants import BLOCK_SIZE

class Frog(arcade.Sprite):

    def __init__(self, img, scaling):
        super().__init__(img, scaling, 0, 0, BLOCK_SIZE, BLOCK_SIZE)

        self.reset()


    def reset(self):
        self.center_x = BLOCK_SIZE * 8 + (BLOCK_SIZE * .5)
        self.center_y = BLOCK_SIZE * 8 + (BLOCK_SIZE * .5)


    def step(self, direction):
        if direction == "LEFT":
            self.center_x -= BLOCK_SIZE
        elif direction == "RIGHT":
            self.center_x += BLOCK_SIZE
        elif direction == "UP":
            self.center_y += BLOCK_SIZE
        elif direction == "DOWN":
            self.center_y -= BLOCK_SIZE


    def die():
        pass    # removes frog from the window