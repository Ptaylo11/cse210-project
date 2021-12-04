import arcade
from game.constants import SCREEN_WIDTH

class Collision_Handler():
    def __main__(self):
        pass

    def check_car_collision(self, frog, car_list, scoreboard):
        if len(arcade.check_for_collision_with_list(frog, car_list)) > 0:

            lives = scoreboard.remove_life_return_total()

            if lives == 0:
                frog.die()
            else:
                frog.reset()
    
    def check_log_collision(self, frog, log_list):
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

    def check_water_collision(self, frog, water_list, scoreboard):
        water_collision = False
        for water in water_list:
            if frog.collides_with_sprite(water):
                water_collision = True

        if water_collision and (frog.get_state() != "LOG"):
            lives = scoreboard.remove_life_return_total()

            if lives == 0:
                frog.die()
            else:
                frog.reset()