from game import constants
import arcade

class HandleCollisionsAction:
    """ Checks if the frog is overlaped by any other sprites.
    Returns true if overlapping, false if not. 
    """
    def check_collision(self):
        if self.frog.collides_with_sprite(Sprite):
            return True
        else:
            return False