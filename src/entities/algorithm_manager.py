from entities.algorithms.human import Human
from entities.algorithms.uniform import Uniform
from entities.algorithms.valuebased import Valuebased


class AlgorithmManager():
    """luokka joka hallinnoi käytössä olevia algoritmeja
    """

    def __init__(self):
        """luokan konstruktori
        """
        self._algorithms = {
            "Human": Human(),
            "Uniform": Uniform(),
            "Valuebased": Valuebased()
        }

    def select_algorithm(self, choice, difficulty):
        """palauttaa valitun algoritmin

        Args:
            choice: algoritmin nimi
            difficulty: algoritmin vaikeustaso

        Returns:
            algoritmi annetuilla tiedoilla
        """
        algorithm = self._algorithms.get(choice)
        algorithm.difficulty = difficulty
        return algorithm

    def list_all(self):
        """palauttaa listan käytössä olevien algoritmien nimistä

        Returns:
            lista käytössä olevien algoritmien nimistä
        """
        return self._algorithms.keys()
