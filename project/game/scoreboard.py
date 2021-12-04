
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
        self._high_score = 0


    def calculate_scoreboard(self):
        """ Displays the amount of lives and the user score
        on the screen.
        """
        
        if self._lives > 1:
            text = f"Score: {self._score} ~ {self._lives} lives left! ~ High score: {self._high_score}"
        elif self._lives == 1:
            text = f"Score: {self._score} ~ {self._lives} life left! ~ High score: {self._high_score}"
        elif self._lives < 1:
            text = f"Score: {self._score} ~ no lives left! ~ High score: {self._high_score}"

        return text


    def remove_life_return_total(self):
        """ Called when the frog collides with a car.
        Removes one life.
        Returns the amount of lives.
        """
        self._lives -= 1
        return self._lives


    def add_points(self, points):
        """ Called when the user progresses farther up on the
        moving screen. Adds points to the score.
        Returns total score.
        """
        self._score += points

        if self._score > self._high_score:
            self._high_score = self._score
        
        return self._score


    def get_high_score(self):
        """ Returns current high score """
        return self._high_score


    def get_lives(self):
        """ Returns current lives """
        return self._lives

    
    def reset(self):
        """ When the game is reset.
        Sets the score to 0
        Sets the lives back to 3
        """
        self._score = 0
        self._lives = 3