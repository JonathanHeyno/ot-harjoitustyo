from entities.game import Game
from entities.player import Player
from entities.algorithm_manager import AlgorithmManager


class GameService():
    def __init__(self):
        self.players = []
        self.player_symbols = []
        self.turn = 0
        self.__number_of_players = 0
        self._winner = -1
        self.game = None

    @property
    def number_of_players(self):
        return self.__number_of_players

    @property
    def board(self):
        return self.game.board

    @property
    def size(self):
        return self.game.size

    @property
    def game_is_over(self):
        return self.game.is_over

    @property
    def game_is_won(self):
        return self.game.is_won

    @property
    def winner_symbol(self):
        if self._winner >= 0:
            return self.player_symbols[self._winner]
        return ''

    @property
    def turn_symbol(self):
        if self.game_is_over:
            return ''
        return self.player_symbols[self.turn]

    def new_game(self, size, how_many_to_win):
        if how_many_to_win > size or how_many_to_win < 0:
            raise ValueError
        self.turn = 0
        self.__number_of_players = 0
        self.players = []
        self.player_symbols = []
        self.game = Game(size, how_many_to_win)
        self._winner = -1

    def add_player(self, name, symbol, str_algorithm, difficulty=0, is_human=True):
        algorithms = AlgorithmManager()
        algorithm = algorithms.select_algorithm(str_algorithm, difficulty)
        self.players.append(Player(name, symbol, algorithm, is_human))
        self.player_symbols.append(symbol)
        self.game.player_symbols = self.player_symbols
        self.__number_of_players += 1

    def add_move_and_get_updates(self, i):
        moves = []
        self.game.add_move((i//self.size), (i % self.size),
                            self.player_symbols[self.turn])
        moves.append((i, self.player_symbols[self.turn]))
        self.turn = (self.turn + 1) % self.__number_of_players
        while not self.players[self.turn].is_human and not self.game.is_over:
            choice = self.players[self.turn].next_move(self.game)
            self.game.add_move(choice[0], choice[1], choice[2])
            moves.append(
                ((choice[0]*self.size + choice[1]), choice[2]))
            self.turn = (self.turn + 1) % self.__number_of_players
        return moves

    def make_computer_moves_and_get_updates(self):
        moves = []

        while not self.players[self.turn].is_human and not self.game.is_over:
            choice = self.players[self.turn].next_move(self.game)

            self.game.add_move(choice[0], choice[1], choice[2])
            moves.append(
            ((choice[0]*self.size + choice[1]), choice[2]))
            self.turn = (self.turn + 1) % self.__number_of_players
        return moves

    def get_winning_row(self):
        winners_as_numbers = []
        winners = self.game.get_winning_row()
        for winner in winners:
            winners_as_numbers.append(winner[0]*self.size + winner[1])
        return winners_as_numbers

    def get_algorithms(self):
        algorithms = AlgorithmManager()
        return list(algorithms.list_all())
