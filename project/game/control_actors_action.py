from game import constants
from game.action import Action
from game.frog import Frog
from game.car import Car

class ControlActorsAction(Action):
    
    
    def __init__(self):
        
        self.actors_dict = {
            "frog": Frog(),
            "car": Car()
        }


    def set_movement(self, actor, direction):
        
        self.actors_dict[actor].step(direction)