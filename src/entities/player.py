class Player():
    def __init__(self, name, symbol, algorithm):
        self.__name = name
        self.__symbol = symbol
        self.__algorithm = algorithm

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    def next_move(self, game):
        coordinates = self.__algorithm.next_move(game, self.__symbol)
        return (coordinates[0], coordinates[1], self.__symbol)
