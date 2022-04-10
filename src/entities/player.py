class Player():
    def __init__(self, name, symbol, algorithm, is_human=True):
        self.__name = name
        self.__symbol = symbol
        self.__algorithm = algorithm
        self.__is_human = is_human

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def is_human(self):
        return self.__is_human

    def next_move(self, game):
        coordinates = self.__algorithm.next_move(game, self.__symbol)
        return (coordinates[0], coordinates[1], self.__symbol)
