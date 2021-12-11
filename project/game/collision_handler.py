import arcade
from game.constants import SCREEN_WIDTH

class Collision_Handler():
    """ 
    Handles any behavior involving collisions.

    Stereotype:
        Controller
    """

    def __init__(self):
        """
        The class constructor. Does not have any variables of its own.
        
        Args:
            self (Collision_Handler): an instance of Collision_Handler
        """
        pass

    def check_car_collision(self, frog, car_list, grass_list, scoreboard):
        """
        Checks for a collision between the frog and a car. If there is one, removes
        a life. If the frog still has lives, resets it and calls ensure_safety().
        
        Args:
            self (Collision_Handler): an instance of Collision_Handler
            frog (Frog): the player-controlled frog
            car_list(Sprite_List): list containing all cars
            grass_list(Sprite_List): list of safe tiles, passed to ensure_safety()
            scoreboard(Scoreboard): keeps track of lives
        """
        if len(arcade.check_for_collision_with_list(frog, car_list)) > 0:

            lives = scoreboard.remove_life_return_total()

            if lives > 0:
                frog.reset()
                self.ensure_safety(frog, grass_list)
    

    def check_log_collision(self, frog, log_list):
        """
        Checks for a collision between the frog and a log. If there is one, changes
        the frog's state to "LOG" and changes its horizontal speed to match the log's. 
        If it isn't, changes the frog's state to its default and sets its horziontal
        speed to 0.
        
        Args:
            self (Collision_Handler): an instance of Collision_Handler
            frog (Frog): the player-controlled frog
            log_list(Sprite_List): list containing all logs
        """
        log_collision = False
        for log in log_list:
            if frog.collides_with_sprite(log):
                frog.change_x = log.change_x
                log_collision = True
                frog.set_state("LOG")

                if frog.left < 0:
                    frog.left = 0
                if frog.right > SCREEN_WIDTH:
                    frog.right = SCREEN_WIDTH

        if not log_collision:
            frog.change_x = 0
            frog.set_state()


    def check_water_collision(self, frog, water_list, grass_list, scoreboard):
        """
        Checks for a collision between the frog and the water. If there is one, sets
        a boolean value to True and then checks if the frog's state. If the state is
        "LOG", nothing happens. If the state is not log, removes a life, resets the frog,
        and calls ensure_safety().
        
        Args:
            self (Collision_Handler): an instance of Collision_Handler
            frog (Frog): the player-controlled frog
            water_list(Sprite_List): list containing all water tiles
            grass_list(Sprite_List): list of safe tiles, passed to ensure_safety()
            scoreboard(Scoreboard): keeps track of lives
        """
        water_collision = False
        for water in water_list:
            if frog.collides_with_sprite(water):
                water_collision = True

        if water_collision and (frog.get_state() != "LOG"):
            lives = scoreboard.remove_life_return_total()

            if lives > 0:
                frog.reset()
                self.ensure_safety(frog, grass_list)


    
    def ensure_safety(self, frog, grass_list):
        """
        Run when the frog is reset to ensure it is set to a safe space.
        Checks for a collision between the frog and a safe tile. If no, 
        moves the frog up a step and loops. If yes, exits the loop.
        
        Args:
            self (Collision_Handler): an instance of Collision_Handler
            frog (Frog): the player-controlled frog
            grass_list(Sprite_List): list of safe tiles
        """
        while(len(arcade.check_for_collision_with_list(frog, grass_list)) <= 0):
            frog.step("UP")