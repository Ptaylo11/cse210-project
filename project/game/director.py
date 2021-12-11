from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCALING, BLOCK_SIZE
from arcade import SpriteList
from game.frog import Frog
from game.scoreboard import Scoreboard
from game.gameboard import Gameboard
from game.collision_handler import Collision_Handler
import arcade


class Director(arcade.Window):
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _game_over (Bool): Whether or not the game has ended
        _paused (Bool): Whether or not the game is paused
        car_list (SpriteList): The car sprite list
        log_list (SpriteList): The log sprite list
        water_list (SpriteList): The water sprite list
        road__list (SpriteList): The road sprite list
        grass_list (SpriteList): The grass sprite list
        all_sprites (SpriteList): A sprite list containing all of the sprites
        frog (Frog): An instance of the frog sprite
        frog_list (SpriteList): The frog sprite list
        scoreboard (Scoreboard): An instance of Scoreboard
        gameboard (Gameboard): An instance of Gameboard
        collision_handler (Collision_Handler): An instance of Collision_Handler
        """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self._game_over = False
        self._paused = False
        self.car_list = SpriteList()
        self.log_list = SpriteList()
        self.water_list = SpriteList()
        self.road_list = SpriteList()
        self.grass_list = SpriteList()
        self.all_sprites = SpriteList()
        self.frog = Frog('project\game\images\\frog.png', SCALING)
        self.frog_list = SpriteList()
        self.scoreboard = Scoreboard()
        self.gameboard = Gameboard()
        self.collision_handler = Collision_Handler()

        #Loads song to be played when game starts : Song credit to @shiru8bit
        self.sound_song = arcade.load_sound('project\game\sounds\\a_little_journey.mp3')

        #Loads death sound
        self.sound_die = arcade.load_sound('project\game\sounds\gameover2.wav')

        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        arcade.set_background_color(arcade.color.WHITE)

        self.gameboard.new_board(self.car_list, self.log_list, self.water_list, self.all_sprites, self.road_list, self.grass_list)
        self.all_sprites.append(self.frog)
        arcade.play_sound(self.sound_song, 1, -1, True)
        self.frog_list.append(self.frog)
        arcade.run()


    def on_key_press(self, key, modifiers):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the frog.

        Args:
            self (Director): An instance of Director
            key (Int): The key that was pressed
            modifiers (Int): The modifier that was pressed
        """
        if key == arcade.key.ESCAPE:
            self._paused = not self._paused

        if key == arcade.key.Q:
            scroll_status = self.gameboard.get_is_scroll()
            self.gameboard.set_is_scroll(not scroll_status)

        if not self._paused:
            if key == arcade.key.W or key == arcade.key.UP:
                self.frog.step("UP")

            elif key == arcade.key.S or key == arcade.key.DOWN:
                self.frog.step("DOWN")

            elif key == arcade.key.A or key == arcade.key.LEFT:
                self.frog.step("LEFT")

            elif key == arcade.key.D or key == arcade.key.RIGHT:
                self.frog.step("RIGHT")

        if self._game_over and (key in (
            arcade.key.W, arcade.key.S, arcade.key.A, arcade.key.D,
            arcade.key.UP, arcade.key.DOWN, arcade.key.LEFT, arcade.key.RIGHT)):
            self._game_over = False
            self.frog.reset()
            self.scoreboard.reset()
            self.gameboard.refresh_board(self.car_list, self.log_list, self.water_list, self.all_sprites, self.road_list, self.grass_list)
            self.collision_handler.ensure_safety(self.frog, self.grass_list)


    def on_update(self, delta_time):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director
            delta_time (time): The amount of time since the function was last called
        """
        if not self._game_over:
            if not self._paused:
                self.all_sprites.update()

                for car in self.car_list:
                    car.loop()
                for log in self.log_list:
                    log.loop()

                self.collision_handler.check_car_collision(self.frog, self.car_list, self.grass_list, self.scoreboard)
                self.collision_handler.check_log_collision(self.frog, self.log_list)
                self.collision_handler.check_water_collision(self.frog, self.water_list, self.grass_list, self.scoreboard)
                
                # Adds points and resets screen when the frog reaches the top block
                if not self.gameboard.get_is_scroll() and self.frog.center_y > (SCREEN_HEIGHT - BLOCK_SIZE):
                    self.frog.reset_y()
                    self.gameboard.refresh_board(self.car_list, self.log_list, self.water_list, self.all_sprites, self.road_list, self.grass_list)
                    self.scoreboard.add_points(160)
                elif self.gameboard.get_is_scroll() and self.frog.center_y > (SCREEN_HEIGHT - BLOCK_SIZE * 7):
                    self.frog.center_y -= BLOCK_SIZE
                    self.gameboard.step(self.car_list, self.log_list, self.water_list, self.all_sprites, self.road_list, self.grass_list)
                    self.scoreboard.add_points(10)

                if self.scoreboard.get_lives() == 0:
                    self._game_over = True
                    arcade.play_sound(self.sound_die)


    def on_draw(self):
        """
        Draws the graphics used in the game.

        Args:
            self (Director): An instance of Director
        """
        arcade.start_render()

        self.water_list.draw()
        self.road_list.draw()
        self.grass_list.draw()
        self.all_sprites.draw()
        self.frog_list.draw()

        #score display
        arcade.draw_text(
            self.scoreboard.calculate_scoreboard(),
            5, SCREEN_HEIGHT - 12, arcade.color.BLACK
        )

        #toggle scroll display
        arcade.draw_text(
            f"Gamemode: {self.gameboard.get_gamemode()} - press Q to toggle. ESC to pause",
            5, SCREEN_HEIGHT - 26, arcade.color.BLACK
        )

        if self._game_over:
            arcade.draw_rectangle_filled(
                SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                BLOCK_SIZE * 10, BLOCK_SIZE * 6,
                arcade.color.WHITE,
            )
            arcade.draw_text(
                "game over :/",
                SCREEN_WIDTH - (BLOCK_SIZE * 13), SCREEN_HEIGHT - (BLOCK_SIZE * 7),
                arcade.color.BLACK, 20, BLOCK_SIZE * 10, "center"
            )
            arcade.draw_text(
                "move to restart",
                SCREEN_WIDTH - (BLOCK_SIZE * 13), SCREEN_HEIGHT - (BLOCK_SIZE * 10),
                arcade.color.BLACK, 16, BLOCK_SIZE * 10, "center"
            )
