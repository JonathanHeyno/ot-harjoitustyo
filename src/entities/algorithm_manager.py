from entities.algorithms.human import Human
from entities.algorithms.uniform import Uniform
from entities.algorithms.valuebased import Valuebased


class AlgorithmManager():
    def __init__(self):
        self._algorithms = {
            "Human": Human(),
            "Uniform": Uniform(),
            "Valuebased": Valuebased()
        }

    def select_algorithm(self, choice, difficulty):
        algorithm = self._algorithms.get(choice)
        algorithm.difficulty = difficulty
        return algorithm

    def list_all(self):
        return self._algorithms.keys()
