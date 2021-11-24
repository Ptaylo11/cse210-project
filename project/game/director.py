from arcade.sprite_list import SpriteList
from game.car import Car
from game.frog import Frog
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCALING, BLOCK_SIZE

import random
import arcade


class Director(arcade.Window):
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        keep_playing: (Bool) whether the game continues or not
        window: (class) the arcade screen window
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._keep_playing = True
        self.window = arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.car_list = SpriteList()
        self.all_sprites = SpriteList()
        self.frog = Frog('project\game\images\\frog.jpeg', SCALING)
        self.lives = 3

        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        arcade.set_background_color(arcade.color.WHITE)
        self.all_sprites.append(self.frog)

        for _ in range(2):
            car = Car(
                "project\game\images\car.png",
                SCALING,
                random.randint(1, SCREEN_WIDTH),
                random.randint(1, SCREEN_HEIGHT),
                BLOCK_SIZE * 2,
                20
            )

            self.car_list.append(car)
            self.all_sprites.append(car)

        arcade.run()

        while self._keep_playing:
            self._do_updates()
            self._do_outputs()

    
    def on_key_press(self, symbol):
        
        if symbol == arcade.key.W:
            self.frog.step("UP")

        elif symbol == arcade.key.S:
            self.frog.step("DOWN")

        elif symbol == arcade.key.A:
            self.frog.step("LEFT")

        elif symbol == arcade.key.D:
            self.frog.step("RIGHT")


    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self.all_sprites.update()
        if self.frog.collides_with_sprite(self.all_sprites):

            self.frog.reset()
            self.lives -= 1

            if self.lives == 0:
                self._keep_playing = False
        

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """

        self.all_sprites.draw()