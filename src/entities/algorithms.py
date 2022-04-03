from entities.human import Human
from entities.uniform import Uniform
from entities.valuebased import Valuebased


class Algorithms():

    #def select_algorithm(self, choice):


    def select_algorithm(self):
        choice = input("Choose player type (Human=H, Uniform=U, Valuebased=V): ").lower()
        algorithms = {
            "h": Human(),
            "u": Uniform(),
            "v": Valuebased()
            }
        return algorithms.get(choice)
