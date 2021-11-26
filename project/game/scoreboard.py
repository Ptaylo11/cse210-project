class Scoreboard:
    """ Keeps track of and displays the user score and the remaining amount """

    def __init__(self):
        self._score = 0
        self._lives = 3

    def display_scoreboard(self):
        """ Displays the amount of lives and the user score
        on the screen.
        """
        pass

    def remove_life(self):
        """ Called when the frog collides with a car.
        Removes one life.
        Returns the amount of lives.
        """

        self._lives -= 1
        return self._lives

    def add_points(self, points):
        """ Called when the user progresses farther up on the
        moving screen. Adds points to the score.
        """
        self._score += points