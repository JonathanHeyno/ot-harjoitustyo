#from random import randint


class Valuebased():

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        self._difficulty = difficulty

    def __on_board(self, x_coord, y_coord, rows, cols):
        if (x_coord >= rows or x_coord < 0 or y_coord >= cols or y_coord < 0):
            return False
        return True

    def __check_if_n_in_direction(self, coords, deltas, board, size, amount):
        rows = size
        cols = size
        while(self.__on_board(coords[0]+deltas[0], coords[1]+deltas[1], rows, cols)
              and board[coords[0]+deltas[0]][coords[1]+deltas[1]] == board[coords[0]][coords[1]]):
            coords[0] += deltas[0]
            coords[1] += deltas[1]
        in_a_row = 1
        while(self.__on_board(coords[0]-deltas[0], coords[1]-deltas[1], rows, cols)
              and board[coords[0]-deltas[0]][coords[1]-deltas[1]] == board[coords[0]][coords[1]]
              and in_a_row < amount):
            in_a_row += 1
            coords[0] -= deltas[0]
            coords[1] -= deltas[1]
        if in_a_row >= amount:
            return True
        return False

    def __check_for_winning_moves(self, how_many_to_win, board, size, symbol):
        winning_moves = []
        for x_coord in range(size):
            for y_coord in range(size):
                #print("x= " + str(x) + " y= "+str(y))
                if board[x_coord][y_coord]:
                    continue
                board[x_coord][y_coord] = symbol
                #print("Asetettiin x= " + str(x) + " y= "+str(y))
                if self.__check_if_n_in_direction([x_coord, y_coord], (1, 0), board,
                                                  size, how_many_to_win):
                    board[x_coord][y_coord] = ""
                    #print("eka iffi. x= " + str(x) + " y= " +str(y))
                    winning_moves.append((x_coord, y_coord))
                elif self.__check_if_n_in_direction([x_coord, y_coord], (0, 1), board,
                                                    size, how_many_to_win):
                    board[x_coord][y_coord] = ""
                    #print("toka iffi. x= " + str(x) + " y= " +str(y))
                    winning_moves.append((x_coord, y_coord))
                elif self.__check_if_n_in_direction([x_coord, y_coord], (1, 1), board,
                                                    size, how_many_to_win):
                    board[x_coord][y_coord] = ""
                    #print("kolmas iffi. x= " + str(x) + " y= " +str(y))
                    winning_moves.append((x_coord, y_coord))
                elif self.__check_if_n_in_direction([x_coord, y_coord], (1, -1), board,
                                                    size, how_many_to_win):
                    board[x_coord][y_coord] = ""
                    #print("neljas iffi. x= " + str(x) + " y= " +str(y))
                    winning_moves.append((x_coord, y_coord))
                else:
                    board[x_coord][y_coord] = ""
        return winning_moves

    def __open_ended_n_in_direction(self, coords, deltas, board,
                                    size, how_many_to_win):
        rows = size
        cols = size
        while(self.__on_board(coords[0]+deltas[0], coords[1]+deltas[1], rows, cols)
              and board[coords[0]+deltas[0]][coords[1]+deltas[1]] == board[coords[0]][coords[1]]):
            coords[0] += deltas[0]
            coords[1] += deltas[1]
        if ((not self.__on_board(coords[0]+deltas[0], coords[1]+deltas[1], rows, cols))
              or board[coords[0]+deltas[0]][coords[1]+deltas[1]]):
            return False
        in_a_row = 1
        while(self.__on_board(coords[0]-deltas[0], coords[1]-deltas[1], rows, cols)
              and board[coords[0]-deltas[0]][coords[1]-deltas[1]] == board[coords[0]][coords[1]]
              and in_a_row < how_many_to_win):
            in_a_row += 1
            coords[0] -= deltas[0]
            coords[1] -= deltas[1]
        if ((not self.__on_board(coords[0]-deltas[0], coords[1]-deltas[1], rows, cols))
              or board[coords[0]-deltas[0]][coords[1]-deltas[1]]):
            return False
        if in_a_row >= how_many_to_win:
            return True
        return False

    def __check_for_open_ended_n_in_row(self, amount, board, size, symbol):
        winning_moves = []
        for x_coord in range(size):
            for y_coord in range(size):
                if board[x_coord][y_coord] != "":
                    continue
                board[x_coord][y_coord] = symbol
                if self.__open_ended_n_in_direction([x_coord, y_coord], (1, 0),
                                                    board, size, amount):
                    board[x_coord][y_coord] = ""
                    winning_moves.append((x_coord, y_coord))
                elif self.__open_ended_n_in_direction([x_coord, y_coord], (0, 1),
                                                      board, size, amount):
                    board[x_coord][y_coord] = ""
                    winning_moves.append((x_coord, y_coord))
                elif self.__open_ended_n_in_direction([x_coord, y_coord], (1, 1),
                                                      board, size, amount):
                    board[x_coord][y_coord] = ""
                    winning_moves.append((x_coord, y_coord))
                elif self.__open_ended_n_in_direction([x_coord, y_coord], (1, -1),
                                                      board, size, amount):
                    board[x_coord][y_coord] = ""
                    winning_moves.append((x_coord, y_coord))
                else:
                    board[x_coord][y_coord] = ""
        return winning_moves



    # Check if there are n in a row with empty spaces at both ends
    def __calculate_points_in_direction(self, coords, deltas,
                                        board, size, how_many_to_win, symbol):
        rows = size
        cols = size
        num = 0
        steps = 1
        points = 0
        while(self.__on_board(coords[0]+deltas[0], coords[1]+deltas[1], rows, cols)
              and (board[coords[0]+deltas[0]][coords[1]+deltas[1]] == symbol
                   or (not board[coords[0]+deltas[0]][coords[1]+deltas[1]]))
              and num < how_many_to_win-1):
            coords[0] += deltas[0]
            coords[1] += deltas[1]
            num += 1
        while num > 0:
            if board[coords[0]][coords[1]] == symbol:
                points += 1
            steps += 1
            num -= 1
            coords[0] -= deltas[0]
            coords[1] -= deltas[1]
        while(self.__on_board(coords[0]-deltas[0], coords[1]-deltas[1], rows, cols)
              and (board[coords[0]-deltas[0]][coords[1]-deltas[1]] == symbol
                   or (not board[coords[0]-deltas[0]][coords[1]-deltas[1]]))
              and num < how_many_to_win):
            coords[0] -= deltas[0]
            coords[1] -= deltas[1]
            num += 1
            steps += 1
            if board[coords[0]][coords[1]] == symbol:
                points += 1
        if steps < how_many_to_win:
            return 0
        return points

    def __calculate_points(self, board, symbol, size, amount, scores):
        for x_coord in range(size):
            for y_coord in range(size):
                if board[x_coord][y_coord]:
                    continue
                board[x_coord][y_coord] = symbol
                scores[x_coord][y_coord] += self.__calculate_points_in_direction(
                    [x_coord, y_coord], (1, 0), board, size, amount, symbol)
                scores[x_coord][y_coord] += self.__calculate_points_in_direction(
                    [x_coord, y_coord], (0, 1), board, size, amount, symbol)
                scores[x_coord][y_coord] += self.__calculate_points_in_direction(
                    [x_coord, y_coord], (1, 1), board, size, amount, symbol)
                scores[x_coord][y_coord] += self.__calculate_points_in_direction(
                    [x_coord, y_coord], (1, -1), board, size, amount, symbol)
                board[x_coord][y_coord] = ""

    def next_move(self, game, symbol):
        board = game.board.copy()
        size = len(board)

        # Check if can win game immediately
        winning_moves = self.__check_for_winning_moves(
            game.how_many_to_win, board, size, symbol)
        if winning_moves:
            return winning_moves[0]

        # Create and initialize score board. Occupied squares have value -1
        scores = [[0 for j in range(size)] for i in range(size)]
        for a_coord in range(size):
            for b_coord in range(size):
                if board[a_coord][b_coord]:
                    scores[a_coord][b_coord] = -1

        # Find out what current player number is
        turn = game.player_symbols.index(symbol)

        # Check if next player can win on next turn and add many points
        # for all winning positions of next player. We do this with points
        # because if there are several such options, we choose the best one
        # and hope opponent does not notice.
        winning_moves = self.__check_for_winning_moves(
            game.how_many_to_win,
            board,
            size,
            game.player_symbols[
                (turn+1) % game.number_of_players
            ]
        )
        if winning_moves:
            for move in winning_moves:
                scores[move[0]][move[1]] += 10000000

        # If only one opponent, check if you can get amount_to_win - 1
        # in a row open-ended, and add several points to all such positions
        if game.number_of_players == 2:
            winning_moves = self.__check_for_open_ended_n_in_row(
                game.how_many_to_win-1, board, size, symbol)
            if winning_moves:
                for move in winning_moves:
                    scores[move[0]][move[1]] += 100000

        # If only one opponent, check he cannot get amount_to_win - 1
        # in a row open-ended, and add extra points to all such positions
        if game.number_of_players == 2:
            winning_moves = self.__check_for_open_ended_n_in_row(
                game.how_many_to_win - 1,
                board, size,
                game.player_symbols[
                    (turn+1) % game.number_of_players
                ]
            )
            if winning_moves:
                for move in winning_moves:
                    scores[move[0]][move[1]] += 1000

        # Calculate points for all squares
        # Go in how_many_to_win given direction
        # Or until hit symbol that is not yours.
        # Then track back to your position +how_many_to_win
        # after that or until hit symbol that is not yours.
        # Sum how many your own symbols were met.
        # Give more points for ones that are connected
        for symb in game.player_symbols:
            self.__calculate_points(
                board, symb, size, game.how_many_to_win, scores)

        # print("Scores:")
        # print(scores)
        # Get squares with highest point score
        highest_scores = []
        max_score = -100
        for x_coord in range(size):
            for y_coord in range(size):
                if scores[x_coord][y_coord] == max_score:
                    highest_scores.append((x_coord, y_coord))
                elif scores[x_coord][y_coord] > max_score:
                    highest_scores = [(x_coord, y_coord)]
                    max_score = scores[x_coord][y_coord]

        # print("highest_scores:")
        # print(highest_scores)
        # If several same, select one in most middle
        minimum_distance = size*size / 1.0
        best_x = -1
        best_y = -1
        for coords in highest_scores:
            dist = ((coords[0]-size//2)**2 + (coords[1]-size//2)**2)**(1/2)
            if dist < minimum_distance:
                minimum_distance = dist
                best_x = coords[0]
                best_y = coords[1]
        return (best_x, best_y)

        #turn = (turn+1)%game.number_of_players
