from arcade import SpriteList
from game.car import Car
from game.frog import Frog
from game.scoreboard import Scoreboard
from game.row import Row
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
        self.car_list = SpriteList()
        self.log_list = SpriteList()
        self.water_list = SpriteList()
        self.all_sprites = SpriteList()
        self.frog = Frog('project\game\images\\frog.jpeg', SCALING)
        self.scoreboard = Scoreboard()
        self.gameboard = []

        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        arcade.set_background_color(arcade.color.WHITE)

        """
        for _ in range(2):
            car = Car(
                "project\game\images\car.png",
                SCALING,
                random.randint(1, SCREEN_WIDTH),
                random.randint(1, 15) * BLOCK_SIZE,
                BLOCK_SIZE * 2,
                5
            )

            self.car_list.append(car)
            self.all_sprites.append(car)

        for _ in range(2):
            log = Car(
                "project\game\images\log.png",
                SCALING,
                random.randint(1, SCREEN_WIDTH),
                random.randint(1, 15) * BLOCK_SIZE,
                BLOCK_SIZE * 4,
                3
            )

            self.log_list.append(log)
            self.all_sprites.append(log)
        """

        for i in range(3):
            self.gameboard.append(
                Row(self.car_list, self.log_list, self.water_list, self.all_sprites, "grass")
            )

            if i > 0:
                for row in self.gameboard:
                    row.step_down()

        for i in range(13):
            self.gameboard.append(
                Row(self.car_list, self.log_list, self.water_list, self.all_sprites)
            )

            for row in self.gameboard:
                row.step_down()
                if row.background.center_y < 0:
                    row.remove_from_sprite_lists()

        
        self.all_sprites.append(self.frog)
        arcade.run()


    def on_key_press(self, key, modifiers):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.
        """
        if key == arcade.key.W:
            self.frog.step("UP")

        elif key == arcade.key.S:
            self.frog.step("DOWN")

        elif key == arcade.key.A:
            self.frog.step("LEFT")

        elif key == arcade.key.D:
            self.frog.step("RIGHT")


    def on_update(self, delta_time):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
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