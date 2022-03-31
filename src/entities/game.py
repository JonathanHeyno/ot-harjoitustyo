class Game:
    def __init__(self, rows, cols, how_many_to_win):
        self.__is_over = False
        self.__is_won = False
        self.__rows = rows
        self.__cols = cols
        self.__board = [[" " for i in range(cols)] for j in range(rows)]
        self.__available_squares = rows*cols
        self.__how_many_to_win = how_many_to_win
        self.__player_symbols = []
        self.__number_of_players = 0


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
        self.__number_of_players = len(player_symbols)

    @property
    def number_of_players(self):
        return self.__number_of_players


    def __on_board(self, x, y):
        if (x >= self.__rows or x < 0 or y >= self.__cols or y < 0):
            return False
        return True

    def __check_if_won_in_direction(self, x, y, dx, dy):        
        while(self.__on_board(x+dx, y+dy) and self.__board[x+dx][y+dy] == self.__board[x][y]):
            x += dx
            y += dy
        in_a_row = 1
        while(self.__on_board(x-dx, y-dy) and self.__board[x-dx][y-dy] == self.__board[x][y] and in_a_row < self.__how_many_to_win):
            in_a_row += 1
            x -= dx
            y -= dy
        if (in_a_row >= self.__how_many_to_win):
            self.__is_over = True
            self.__is_won = True

    def __update_status(self, x, y):
        if (self.__available_squares == 0):
            self.__is_over = True
        self.__check_if_won_in_direction(x, y, 1, 0)
        self.__check_if_won_in_direction(x, y, 0, 1)
        self.__check_if_won_in_direction(x, y, 1, 1)
        self.__check_if_won_in_direction(x, y, 1, -1)

    def add_move(self, x, y, symbol):
        if (self.__is_over):
            raise IndexError("Game is over")
        elif (not isinstance(x, int) or not isinstance(y, int)):
            raise TypeError("Integer value required")
        elif (not self.__on_board(x, y)):
            raise IndexError("Off board")
        elif (self.__board[x][y] != " "):
            raise ValueError("Space not empty")
        else:
            self.__board[x][y] = symbol
            self.__available_squares -= 1
            self.__update_status(x, y)
