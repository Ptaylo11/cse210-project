from arcade import SpriteList
from game.frog import Frog
from game.scoreboard import Scoreboard
from game.gameboard import Gameboard
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCALING
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
        self.scoreboard = Scoreboard()
        self.gameboard = Gameboard()

        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        arcade.set_background_color(arcade.color.WHITE)

        self.gameboard.new_board(self.car_list, self.log_list, self.water_list, self.all_sprites, self.road_and_grass_list)
        self.all_sprites.append(self.frog)

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


            #check_for_collision_with_list returns a list, so we check if the list is empty
            if len(arcade.check_for_collision_with_list(self.frog, self.car_list)) > 0:

                lives = self.scoreboard.remove_life_return_total()

                if lives == 0:
                    self._keep_playing = False
                    self.frog.die()
                else:
                    self.frog.reset()



            #checks for if riding log or not, and changes frog's change_x to match log speed if true
            log_collision = False
            for log in self.log_list:
                if self.frog.collides_with_sprite(log):
                    self.frog.change_x = log.change_x
                    log_collision = True

                    if self.frog.left < 0:
                        self.frog.left = 0
                    if self.frog.right > SCREEN_WIDTH:
                        self.frog.right = SCREEN_WIDTH

            if not log_collision:
                self.frog.change_x = 0

            #checks for water collision while not riding log
            water_collision = False
            for water in self.water_list:
                if self.frog.collides_with_sprite(water):
                    water_collision = True

            if water_collision and not log_collision:
                lives = self.scoreboard.remove_life_return_total()

                if lives == 0:
                    self._keep_playing = False
                    self.frog.die()
                else:
                    self.frog.reset()

        
    def on_draw(self):
        arcade.start_render()

        self.water_list.draw()
        self.road_and_grass_list.draw()
        self.all_sprites.draw()

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