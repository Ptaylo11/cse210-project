from arcade import SpriteList
from game.frog import Frog
from game.scoreboard import Scoreboard
from game.gameboard import Gameboard
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCALING, BLOCK_SIZE
from game.collision_handler import Collision_Handler
import arcade


class Director(arcade.Window):
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        keep_playing: (Bool) whether the game continues or not
        car_list: instance of SpriteList
        log_list: instance of SpriteList
        all_sprites: instance of SpriteList
        frog: instance of Frog
        scoreboard: instance of Scoreboard
        gameboard: array of instances of Row
    """


    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self._keep_playing = True
        self._paused = False
        self.car_list = SpriteList()
        self.log_list = SpriteList()
        self.water_list = SpriteList()
        self.road_and_grass_list = SpriteList()
        self.all_sprites = SpriteList()
        self.frog = Frog('project\game\images\\frog.png', SCALING)
        self.frog_list = SpriteList()
        self.scoreboard = Scoreboard()
        self.gameboard = Gameboard()
        self.collision_handler = Collision_Handler()

        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        arcade.set_background_color(arcade.color.WHITE)

        self.gameboard.new_board(self.car_list, self.log_list, self.water_list, self.all_sprites, self.road_and_grass_list)
        self.all_sprites.append(self.frog)
        self.frog_list.append(self.frog)

        arcade.run()


    def on_key_press(self, key, modifiers):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.
        """
        if key == arcade.key.ESCAPE:
            self._paused = not self._paused

        if not self._paused:
            if key == arcade.key.W or key == arcade.key.UP:
                self.frog.step("UP")

            elif key == arcade.key.S or key == arcade.key.DOWN:
                self.frog.step("DOWN")

            elif key == arcade.key.A or key == arcade.key.LEFT:
                self.frog.step("LEFT")

            elif key == arcade.key.D or key == arcade.key.RIGHT:
                self.frog.step("RIGHT")


    def on_update(self, delta_time):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        if not self._paused:
            self.all_sprites.update()

            for car in self.car_list:
                car.loop()
            for log in self.log_list:
                log.loop()

            self.collision_handler.check_car_collision(self.frog, self.car_list, self.scoreboard)
            self.collision_handler.check_log_collision(self.frog, self.log_list)
            self.collision_handler.check_water_collision(self.frog, self.water_list, self.scoreboard)

            # Adds points and resets screen when the frog reaches the top block
            if self.frog.center_y > (SCREEN_HEIGHT - BLOCK_SIZE):
                self.frog.reset_y()
                self.gameboard.refresh_board(self.car_list, self.log_list, self.water_list, self.all_sprites, self.road_and_grass_list)
                self.scoreboard.add_points_and_return(100)

        
    def on_draw(self):
        arcade.start_render()

        self.water_list.draw()
        self.road_and_grass_list.draw()
        self.all_sprites.draw()
        self.frog_list.draw()

        #score display
        if self._keep_playing:
            text = self.scoreboard.calculate_scoreboard()
        else:
            text = "game over!"

        arcade.draw_text(
            text,
            5,
            SCREEN_HEIGHT - 12,
            arcade.color.BLACK
        )