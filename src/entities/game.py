class Game:
    """Luokka joka pitää yllä pelin tilannetta

    Attributes:
        is_won: boolean, onko peli voitettu
        is_over: boolean, onko peli ohi
        size: pelilaudan koko
        board: pelilauta jossa pelatut symbolit vastaavissa koordinaateissa
        how_many_to_win: montaako pitää saada jonoon voittoon
        player_symbols: lista pelaajien symboleista
        number_of_players: pelaajien määrä
    """
    def __init__(self, size, how_many_to_win):
        self.__is_over = False
        self.__is_won = False
        self.__size = size
        self.__board = [["" for i in range(size)] for j in range(size)]
        self.__available_squares = size*size
        self.__how_many_to_win = how_many_to_win
        self.__player_symbols = []

    @property
    def is_won(self):
        return self.__is_won

    @is_won.setter
    def is_won(self, is_won):
        if not isinstance(is_won, bool):
            raise TypeError("Boolean value required")
        self.__is_won = is_won

    @property
    def is_over(self):
        return self.__is_over

    @is_over.setter
    def is_over(self, is_over):
        if not isinstance(is_over, bool):
            raise TypeError("Boolean value required")
        self.__is_over = is_over

    @property
    def size(self):
        return self.__size

    @property
    def board(self):
        return self.__board

    @property
    def how_many_to_win(self):
        return self.__how_many_to_win

    @property
    def player_symbols(self):
        return self.__player_symbols

    @player_symbols.setter
    def player_symbols(self, player_symbols):
        self.__player_symbols = player_symbols
        #self.__number_of_players = len(player_symbols)

    @property
    def number_of_players(self):
        #return self.__number_of_players
        return len(self.player_symbols)

    def __on_board(self, x_coord, y_coord):
        if (x_coord >= self.__size or x_coord < 0 or y_coord >= self.__size or y_coord < 0):
            return False
        return True

    def __check_if_won_in_direction(self, x_coord, y_coord, delta_x, delta_y):
        if not self.__board[x_coord][y_coord]:
            return []
        while(self.__on_board(x_coord+delta_x, y_coord+delta_y)
              and self.__board[x_coord+delta_x][y_coord+delta_y]
              == self.__board[x_coord][y_coord]):
            x_coord += delta_x
            y_coord += delta_y
        in_a_row = 1
        winners = []
        winners.append((x_coord, y_coord))
        while(self.__on_board(x_coord-delta_x, y_coord-delta_y)
              and self.__board[x_coord-delta_x][y_coord-delta_y] == self.__board[x_coord][y_coord]
              and in_a_row < self.__how_many_to_win):
            in_a_row += 1
            x_coord -= delta_x
            y_coord -= delta_y
            winners.append((x_coord, y_coord))
        if in_a_row >= self.__how_many_to_win:
            self.__is_over = True
            self.__is_won = True
            return winners
        return []

    def __update_status(self, x_coord, y_coord):
        if self.__available_squares == 0:
            self.__is_over = True
        self.__check_if_won_in_direction(x_coord, y_coord, 1, 0)
        self.__check_if_won_in_direction(x_coord, y_coord, 0, 1)
        self.__check_if_won_in_direction(x_coord, y_coord, 1, 1)
        self.__check_if_won_in_direction(x_coord, y_coord, 1, -1)

    def move_is_allowed(self, x_coord, y_coord):
        """palauttaa tiedon onko siirto sallittu

        Args:
            x_coord: x-koordinaatti
            y_coord: y-koordinaatti

        Returns:
            boolean, onko siirto sallittu
        """
        return ((not self.__is_over)
            and isinstance(x_coord, int)
            and isinstance(y_coord, int)
            and self.__on_board(x_coord, y_coord)
            and (not self.__board[x_coord][y_coord]))

    def add_move(self, x_coord, y_coord, symbol):
        """lisää siirron laudalle jos se on sallittu siirto

        Args:
            x_coord: x-koordinaatti
            y_coord: y-koordinaatti
            symbol: ruutuun laitettava symboli
        """
        if self.move_is_allowed(x_coord, y_coord):
            self.__board[x_coord][y_coord] = symbol
            self.__available_squares -= 1
            self.__update_status(x_coord, y_coord)

    def get_winning_row(self):
        """palauttaa voittavan trivin jos peli on voitettu

        Returns:
            lista voittavien ruutujen koordinaateista
        """
        winners = []
        for i in range(self.__size):
            for j in range(self.__size):
                winners += self.__check_if_won_in_direction(i, j, 1, 0)
                winners += self.__check_if_won_in_direction(i, j, 0, 1)
                winners += self.__check_if_won_in_direction(i, j, 1, 1)
                winners += self.__check_if_won_in_direction(i, j, 1, -1)

        duplicates_removed = []
        for winner in winners:
            if winner not in duplicates_removed:
                duplicates_removed.append(winner)

        return duplicates_removed
