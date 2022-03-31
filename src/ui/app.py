from entities.game import Game
from entities.player import Player
from entities.algorithms import Algorithms


class App():
    def __init__(self):
        self.__players = []

    def __start(self):
        print("\nNew game\nLoad game\nSave game\nQuit\n")
        choice = input("N/L/S/Q: ").lower()
        return choice 

    def __create_new_player(self):
        name = input("Name: ")
        symbol = input("Symbol: ")
        algorithms = Algorithms()
        algorithm = algorithms.select_algorithm()
        self.__players.append(Player(name, symbol, algorithm))
    
    def __get_players(self):
        self.__number_of_players = int(input("Number of players: "))
        for i in range (self.__number_of_players):
            print("\nPlayer: "+str(i+1))
            self.__create_new_player()
            '''
            choice = ""
            while choice != "n" and choice != "c":
                choice = input("N = New Player,  S = Select player: ").lower()
                if choice == "n":
                    self.__create_new_player()
            '''


    def __new_game(self):
        self.__players = []
        self.__get_players()       
        size = int(input("Size of board: "))
        self.__rows = size
        self.__cols = size
        how_many_to_win = int(input("How many to win: "))
        self.__game = Game(size, size, how_many_to_win)
        player_symbols = []
        for player in self.__players:
            player_symbols.append(player.symbol)
        self.__game.player_symbols = player_symbols

    def __draw(self):
        board = self.__game.board
        for i in range(self.__rows):
            line = ""
            line2 = ""
            for j in range(self.__cols):
                line += "|" + board[i][j]
                line2 += "--"
            print(line+"|")
            print(line2+"-")
        print("\n")


    def run(self):
        while True:
            choice = ""
            while choice != "n" and choice != "l" and choice != "s" and choice != "q":
                choice = self.__start()
            if choice == "q":
                break
            if choice == "n":
                self.__new_game()
            
            player = 0
            self.__draw()

            while True:
                choice = self.__players[player].next_move(self.__game)
                try:
                    self.__game.add_move(choice[0], choice[1], choice[2])
                    player = (player+1) % self.__number_of_players
                except:
                    print("Invalid choice")
                self.__draw()
                if self.__game.is_over:
                    print ("Game is over")
                    #self.__players = []
                    if self.__game.is_won:
                        print("Game is won")
                    break
