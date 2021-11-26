
class Scoreboard:
    """ Keeps track of and displays the user score and the remaining amount
    """

    def __init__(self):
        """ The class constructor. Has 2 attributes:
        score: (int)
        lives: (int) - starts with 3
        """

        self._score = 0
        self._lives = 3


    def calculate_scoreboard(self):
        """ Displays the amount of lives and the user score
        on the screen.
        """
        
        if self._lives > 1:
            text = f"Score: {self._score} ~ {self._lives} lives left!"
        elif self._lives == 1:
            text = f"Score: {self._score} ~ {self._lives} life left!"
        elif self._lives < 1:
            text = f"Score: {self._score} ~ no lives left!"

        return text


    def remove_life_return_total(self):
        """ Called when the frog collides with a car.
        Removes one life.
        Returns the amount of lives.
        """
        self._lives -= 1
        return self._lives


    def add_points_and_return(self, points):
        """ Called when the user progresses farther up on the
        moving screen. Adds points to the score.
        Returns total score.
        """
        self._score += points
        return self._score      # likely the only use for this return is debugging purposes...