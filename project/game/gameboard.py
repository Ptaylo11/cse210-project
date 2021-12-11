from game.row import Row


class Gameboard:
    """ Represents the board used in the game.
    Screen dimentions:
    Height -- 16 X BLOCK_SIZE
    Width -- 16 X BLOCK_SIZE

    Stereotype:
        Information Holder

    Attributes:
        _rows (List): The list of each row. Can be a grass, water, or road row and can contain logs, cars,
            and the frog.
        is_scrolling (Bool): Whether or not the game is in scrolling mode.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Gameboard): an instance of Gameboard.
        """
        self._rows = []
        self.is_scrolling = False


    def get_is_scroll(self):
        """ returns if the screen is set to scroll or not.
        If not scroll the screen will move like a page.

        Args:
            self (Gameboard): an instance of Gameboard.
        """
        return self.is_scrolling


    def set_is_scroll(self, bool):
        """ Changes the gamemode to either scroll or not.

        Args:
            self (Gameboard): an instance of Gameboard.
            bool (Bool): the boolean to set is_scrolling to.
        """
        self.is_scrolling = bool

    
    def get_gamemode(self):
        """ retrieves the current gamemode (SCROLL or LEVEL) and returns it.

        Args:
            self (Gameboard): an instance of Gameboard.
        """
        if self.get_is_scroll():
            gamemode = "SCROLL"
        else:
            gamemode = "PAGE"

        return gamemode


    def step(self, car_list, log_list, water_list, all_sprites, road_and_grass_list):
        """ This steps every row and it's sprites down one block length.
        Then, a new generic row is generated at the top (random theme).

        Args:
            self (Gameboard): an instance of Gameboard.
            car_list (SpriteList): the list of car Sprites.
            log_list (SpriteList): the list of log Sprites.
            water_list (SpriteList): the list of water Sprites.
            all_sprites (SpriteList): the list containing all of the Sprites in the game.
            road_and_grass_list (SpriteList): the list of road and grass Sprites.
        """
        # steps every existing row down one block
        for row in self._rows:
            row.step_down()

        # generates a new row at the top block of the screen
        self._rows.append(
            Row(car_list, log_list, water_list, all_sprites, road_and_grass_list)
        )

    def step_grass(self, car_list, log_list, water_list, all_sprites, road_and_grass_list):
        """ This steps every row and it's sprites down one block length.
        Then, a new generic row is generated at the top (random theme).

        Args:
            self (Gameboard): an instance of Gameboard.
            car_list (SpriteList): the list of car Sprites.
            log_list (SpriteList): the list of log Sprites.
            water_list (SpriteList): the list of water Sprites.
            all_sprites (SpriteList): the list containing all of the Sprites in the game.
            road_and_grass_list (SpriteList): the list of road and grass Sprites.
        """
        # steps every existing row down one block
        for row in self._rows:
            row.step_down()

        # generates a new row at the top block of the screen
        self._rows.append(
            Row(car_list, log_list, water_list, all_sprites, road_and_grass_list, "grass")
        )


    def new_board(self, car_list, log_list, water_list, all_sprites, road_and_grass_list):
        """ Generates a starting game board. This board consists of:
                3 rows of grass
                12 rows
        
        Args:
            self (Gameboard): an instance of Gameboard.
            car_list (SpriteList): the list of car Sprites.
            log_list (SpriteList): the list of log Sprites.
            water_list (SpriteList): the list of water Sprites.
            all_sprites (SpriteList): the list containing all of the Sprites in the game.
            road_and_grass_list (SpriteList): the list of road and grass Sprites.
        """

        # generates the first 3 rows as grass
        for _ in range(3):
            self.step_grass(car_list, log_list, water_list, all_sprites, road_and_grass_list)

        # generates the next 12 rows. Theme is randomly selected in the Row constructor
        for _ in range(12):
            self.step(car_list, log_list, water_list, all_sprites, road_and_grass_list)

        # generates the last row (16th) as grass
        self.step_grass(car_list, log_list, water_list, all_sprites, road_and_grass_list)

    
    def refresh_board(self, car_list, log_list, water_list, all_sprites, road_and_grass_list):
        """ Refreshing the board means making a new board.
        However, the bottom row needs to be the same as the previous top row.
        Calls the self.step method 14 times, then the self.step_grass method once.

        Args:
            self (Gameboard): an instance of Gameboard.
            car_list (SpriteList): the list of car Sprites.
            log_list (SpriteList): the list of log Sprites.
            water_list (SpriteList): the list of water Sprites.
            all_sprites (SpriteList): the list containing all of the Sprites in the game.
            road_and_grass_list (SpriteList): the list of road and grass Sprites.
        """

        for _ in range(14):
            self.step(car_list, log_list, water_list, all_sprites, road_and_grass_list)

        self.step_grass(car_list, log_list, water_list, all_sprites, road_and_grass_list)