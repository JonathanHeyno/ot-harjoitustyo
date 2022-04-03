from random import choice

class Uniform():
    def next_move(self, game, symbol):
        choices = []
        square = 0
        size = len(game.board)
        for i in range(size):
            for j in range(size):
                if game.board[i][j] == " ":
                    choices.append(square)
                square += 1
        square = choice(choices)
        return ((square // size), (square % size))
