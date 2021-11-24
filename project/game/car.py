import arcade
import random
from game.constants import BLOCK_SIZE, SCREEN_WIDTH

class Car(arcade.Sprite):

    def __init__(self, img, scaling, x, y, width, speed):
        super().__init__(img, scaling, 0, 0, width, BLOCK_SIZE)

        self.center_x = x
        self.center_y = y
        self.change_x = speed

    def loop(self):
        if self.center_x > SCREEN_WIDTH + self.width:
            self.center_x = 0 - self.width
        elif self.center_x < 0 - self.width:
            self.center_x = SCREEN_WIDTH + self.width