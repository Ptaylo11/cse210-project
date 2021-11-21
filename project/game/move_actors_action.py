from game.action import Action
import arcade

class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller
    """

    def move_sprites(self):
        """Moves the sprites in the given sprite list to their next position
        according to their velocity.

        Args:
            sprite_list (Sprite List): The sprite list of all sprites that need to be moved.
        """
        arcade.SpriteList.update()