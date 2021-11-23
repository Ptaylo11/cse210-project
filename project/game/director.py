from arcade.sprite_list.sprite_list import SpriteList
from game.control_actors_action import ControlActorsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCALING

import random
import arcade

from game.car import Car
from game.frog import Frog
from game.constants import BLOCK_SIZE

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
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.car_list = SpriteList()
        self.all_sprites = SpriteList()

        self.start_game()

        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        arcade.set_background_color(arcade.color.WHITE)

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
        
        frog = Frog('project\game\images\\frog.jpeg', SCALING)
        self.all_sprites.append(frog)


    def on_key_press(self, key, modifiers):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        #frog_movement = InputService.check_for_input()
        
        #if frog_movement is not None:
        #    ControlActorsAction.set_movement("frog", frog_movement)

        InputService.on_key_press(InputService, Frog, key, modifiers)


    def update(self, delta_time):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        # MoveActorsAction.move_sprites()

        self.all_sprites.update()

        for car in self.car_list:
            car.loop()


        
    def on_draw(self):
        arcade.start_render()

        self.all_sprites.draw()