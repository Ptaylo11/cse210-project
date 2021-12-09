
class Scoreboard:
    """ Keeps track of and displays the user score and the remaining amount of lives.

    Stereotype:
        Information Holder
    
    Attributes:
        _score (Int): The user's current score
        _lives (Int): The remaining amount of lives
        _high_score (Int): The user's high score as of running the program
    """

    def __init__(self):
        """ The class constructor.

        Args:
            self (Scoreboard): An instance of Scoreboard
        """

        self._score = 0
        self._lives = 3
        self._high_score = 0


    def calculate_scoreboard(self):
        """ Displays the amount of lives and the user score
        on the screen.

        Args:
            self (Scoreboard): An instance of Scoreboard
        """
        
        if self._lives > 1:
            text = f"Score: {self._score} ~ {self._lives} lives left! ~ High score: {self._high_score}"
        elif self._lives == 1:
            text = f"Score: {self._score} ~ {self._lives} life left! ~ High score: {self._high_score}"
        elif self._lives < 1:
            text = f"Score: {self._score} ~ no lives left! ~ High score: {self._high_score}"

        return text


    def remove_life_return_total(self):
        """ Called when the frog collides with a car. Removes a life and returns the remaining number
        of lives.

        Args:
            self (Scoreboard): An instance of Scoreboard
        
        Returns:
            Int
        """
        self._lives -= 1
        return self._lives


    def add_points(self, points):
        """ Called when the user progresses farther up on the moving screen. Adds points to the score and
        returns the total score.

        Args:
            self (Scoreboard): An instance of Scoreboard
            points (Int): The total points the user has earned
        
        Returns:
            Int
        """
        self._score += points

        if self._score > self._high_score:
            self._high_score = self._score
        
        return self._score


    def get_high_score(self):
        """ Returns the current high score as of running the program.
        
        Args:
            self (Scoreboard): An instance of Scoreboard
        
        Returns:
            Int
        """
        return self._high_score


    def get_lives(self):
        """ Returns the current number of lives.
        
        Args:
            self (Scoreboard): An instance of Scoreboard

        Returns:
            Int
        """
        return self._lives

    
    def reset(self):
        """ When the game is reset. Sets the score to 0 and sets the lives back to 3.
        
        Args:
            self (Scoreboard): An instance of Scoreboard
        """
        self._score = 0
        self._lives = 3