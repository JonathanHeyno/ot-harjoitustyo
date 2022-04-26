class Player():
    """pelaaja jolle liitetään nii, pelisymboli ja algoritmi
    Attributes:
        name: pelaajan nimi
        symbol: pelaajan pelisymboli
        is_human: boolean, onko kyseessä ihminen
        difficulty: pelaajan/algoritmin vaikeustaso
        str_algorithm: algoritmin nimi stringinä
    """
    def __init__(self, name, symbol, algorithm, str_algorithm, difficulty, is_human=True):
        """luokan konstruktori

        Args:
            name: pelaajan nimi
            symbol: pelaajan pelisymboli
            algorithm: algoritmi jolla pelaaja määrittää siirron
            str_algorithm: algoritmin nimi stringinä
            difficulty: pelaajan/algoritmin vaikeustaso
            is_human: boolean, onko pelaaja ihminen
        """
        self.__name = name
        self.__symbol = symbol
        self.__algorithm = algorithm
        self.__str_algorithm = str_algorithm
        self.__difficulty = difficulty
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

    @property
    def difficulty(self):
        return self.__difficulty

    @property
    def str_algorithm(self):
        return self.__str_algorithm

    def next_move(self, game):
        """hakee seuraavan pelisiirron algoritmiltä

        Args:
            game: peli-olio

        Returns:
            valitun ruudun koordinaatit ja pelisymboli
        """
        coordinates = self.__algorithm.next_move(game, self.__symbol)
        return (coordinates[0], coordinates[1], self.__symbol)
