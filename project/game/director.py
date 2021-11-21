from game.control_actors_action import ControlActorsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

import arcade

class Director:
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
        self.window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        arcade.run()

        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()


    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        frog_movement = InputService.check_for_input()
        
        if frog_movement is not None:
            ControlActorsAction.set_movement("frog", frog_movement)


    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        # MoveActorsAction.move_sprites()

        arcade.SpriteList.update()

        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        # OutputService.draw_sprites()

        arcade.SpriteList.draw()