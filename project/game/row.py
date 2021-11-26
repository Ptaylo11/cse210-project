import random
from game.mover import Mover
from game.background import Background


class Row:
    """ Represents one row of the game.
    Each row has two main elements:
    Background - instance of Background()
    Mover - instance of Mover()
    """

    def __init__(self, car_list, log_list, water_list, all_sprites, theme=None):
        """ The class constuctor. Randomizes the theme and
        creates a row to match.
        Attributes:
        theme: Str
        background: instance of Background
        mover: instance of Mover
        """
        if theme == "grass":
            self.theme = theme
        else:
            self.theme = random.choice(["grass", "road", "water"])
        
        self.background = Background(self.theme)
        self.mover = Mover(self.theme)

        if self.theme == "road":
            all_sprites.append(self.mover)
            car_list.append(self.mover)
        elif self.theme == "water":
            water_list.append(self.background)
            all_sprites.append(self.mover)
            log_list.append(self.mover)


    def step_down(self):
        """ Moves the whole row and everything in it one block-size down.
        """

        self.background.step_down()
        self.mover.step_down()