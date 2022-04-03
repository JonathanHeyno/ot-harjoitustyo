from random import randint

class Valuebased():

    def __on_board(self, x, y, rows, cols):
        if (x >= rows or x < 0 or y >= cols or y < 0):
            return False
        return True


    def __check_if_n_in_direction(self, x, y, dx, dy, board, size, n):
        rows = size
        cols = size
        while(self.__on_board(x+dx, y+dy, rows, cols) and board[x+dx][y+dy] == board[x][y]):
            x += dx
            y += dy
        in_a_row = 1
        while(self.__on_board(x-dx, y-dy, rows, cols) and board[x-dx][y-dy] == board[x][y] and in_a_row < n):
            in_a_row += 1
            x -= dx
            y -= dy
        if (in_a_row >= n):
            return True
        return False



    def __check_for_winning_moves(self, how_many_to_win, board, size, symbol):
        winning_moves = []
        for x in range(size):
            for y in range(size):
                #print("x= " + str(x) + " y= "+str(y))
                if board[x][y] != " ":
                    continue
                board[x][y] = symbol
                #print("Asetettiin x= " + str(x) + " y= "+str(y))
                if (self.__check_if_n_in_direction(x, y, 1, 0, board, size, how_many_to_win)):
                    board[x][y] = " "
                    #print("eka iffi. x= " + str(x) + " y= " +str(y))
                    winning_moves.append((x, y))
                elif self.__check_if_n_in_direction(x, y, 0, 1, board, size, how_many_to_win):
                    board[x][y] = " "
                    #print("toka iffi. x= " + str(x) + " y= " +str(y))
                    winning_moves.append((x, y))
                elif self.__check_if_n_in_direction(x, y, 1, 1, board, size, how_many_to_win):
                    board[x][y] = " "
                    #print("kolmas iffi. x= " + str(x) + " y= " +str(y))
                    winning_moves.append((x, y))
                elif self.__check_if_n_in_direction(x, y, 1, -1, board, size, how_many_to_win):
                    board[x][y] = " "
                    #print("neljas iffi. x= " + str(x) + " y= " +str(y))
                    winning_moves.append((x, y))
                else:
                    board[x][y] = " "
        return winning_moves

    #Check if there n in a row with empty spaces at both ends
    def __open_ended_n_in_direction(self, x, y, dx, dy, board, size, how_many_to_win):
        rows = size
        cols = size
        while(self.__on_board(x+dx, y+dy, rows, cols) and board[x+dx][y+dy] == board[x][y]):
            x += dx
            y += dy
        if ((not self.__on_board(x+dx, y+dy, rows, cols)) or board[x+dx][y+dy] != " "):
            return False
        in_a_row = 1
        while(self.__on_board(x-dx, y-dy, rows, cols) and board[x-dx][y-dy] == board[x][y] and in_a_row < how_many_to_win):
            in_a_row += 1
            x -= dx
            y -= dy
        if ((not self.__on_board(x-dx, y-dy, rows, cols)) or board[x-dx][y-dy] != " "):
            return False
        if (in_a_row >= how_many_to_win):
            return True
        return False

    def __check_for_open_ended_n_in_row(self, n, board, size, symbol):
        winning_moves = []
        for x in range(size):
            for y in range(size):
                if board[x][y] != " ":
                    continue
                board[x][y] = symbol
                if (self.__open_ended_n_in_direction(x, y, 1, 0, board, size, n)):
                    board[x][y] = " "
                    winning_moves.append((x, y))
                elif self.__open_ended_n_in_direction(x, y, 0, 1, board, size, n):
                    board[x][y] = " "
                    winning_moves.append((x, y))
                elif self.__open_ended_n_in_direction(x, y, 1, 1, board, size, n):
                    board[x][y] = " "
                    winning_moves.append((x, y))
                elif self.__open_ended_n_in_direction(x, y, 1, -1, board, size, n):
                    board[x][y] = " "
                    winning_moves.append((x, y))
                else:
                    board[x][y] = " "
        return winning_moves


    def __calculate_points_in_direction(self, x, y, dx, dy, board, size, how_many_to_win, symbol):
        rows = size
        cols = size
        n = 0
        steps = 1
        points = 0
        while(self.__on_board(x+dx, y+dy, rows, cols) and (board[x+dx][y+dy] == symbol or board[x+dx][y+dy] == " ") and n < how_many_to_win-1):
            x += dx
            y += dy
            n += 1
        while n > 0:
            if (board[x][y] == symbol):
                points += 1
            steps += 1
            n -= 1
            x -= dx
            y -= dy
        while(self.__on_board(x-dx, y-dy, rows, cols) and (board[x-dx][y-dy] == symbol or board[x-dx][y-dy] == " ") and n < how_many_to_win):
            x -= dx
            y -= dy
            n += 1
            steps += 1
            if (board[x][y] == symbol):
                points += 1
        if steps < how_many_to_win:
            return 0
        return points


    def __calculate_points(self, board, symbol, size, n, scores):
        for x in range(size):
            for y in range(size):
                if board[x][y] != " ":
                    continue
                board[x][y] = symbol
                scores[x][y] += self.__calculate_points_in_direction(x, y, 1, 0, board, size, n, symbol)
                scores[x][y] += self.__calculate_points_in_direction(x, y, 0, 1, board, size, n, symbol)
                scores[x][y] += self.__calculate_points_in_direction(x, y, 1, 1, board, size, n, symbol)
                scores[x][y] += self.__calculate_points_in_direction(x, y, 1, -1, board, size, n, symbol)
                board[x][y] = " "



    def next_move(self, game, symbol):
        board = game.board.copy()
        size = len(board)

        #Check if can win game immediately
        winning_moves = self.__check_for_winning_moves(game.how_many_to_win, board, size, symbol)
        if winning_moves:
            return winning_moves[0]
        
        #Create and initialize score board. Occupied squares have value -1
        scores = [[0 for j in range(size)] for i in range(size)]
        for a in range(size):
            for b in range(size):
                if board[a][b] != " ":
                    scores[a][b] = -1


        #Find out what current player number is
        turn = game.player_symbols.index(symbol)


        #Check if next player can win on next turn and add many points
        #for all winning positions of next player. We do this with points
        #because if there are several such options, we choose the best one
        #and hope opponent does not notice.
        winning_moves = self.__check_for_winning_moves(
                                                    game.how_many_to_win,
                                                    board,
                                                    size,
                                                    game.player_symbols[
                                                        (turn+1)%game.number_of_players
                                                        ]
                                                    )
        if winning_moves:
            for move in winning_moves:
                scores[move[0]][move[1]] += 10000000


        #If only one opponent, check if you can get amount_to_win - 1
        #in a row open-ended, and add several points to all such positions
        if game.number_of_players == 2:
            winning_moves = self.__check_for_open_ended_n_in_row(game.how_many_to_win-1, board, size, symbol)
            if winning_moves:
                for move in winning_moves:
                    scores[move[0]][move[1]] += 100000


        #If only one opponent, check he cannot get amount_to_win - 1
        #in a row open-ended, and add extra points to all such positions
        if game.number_of_players == 2:
            winning_moves = self.__check_for_open_ended_n_in_row(
                                                                game.how_many_to_win - 1,
                                                                board, size,
                                                                game.player_symbols[
                                                                                    (turn+1)%game.number_of_players
                                                                                    ]
                                                                )
            if winning_moves:
                for move in winning_moves:
                    scores[move[0]][move[1]] += 1000





        #Calculate points for all squares
        #Go in how_many_to_win given direction
        #Or until hit symbol that is not yours.
        #Then track back to your position +how_many_to_win
        #after that or until hit symbol that is not yours.
        #Sum how many your own symbols were met.
        #Give more points for ones that are connected
        for symb in game.player_symbols:
            self.__calculate_points(board, symb, size, game.how_many_to_win, scores)




        #print("Scores:")
        #print(scores)
        #Get squares with highest point score
        highest_scores = []
        max_score = -100
        for x in range(size):
            for y in range(size):
                if scores[x][y] == max_score:
                    highest_scores.append((x, y))
                elif scores[x][y] > max_score:
                    highest_scores = [(x, y)]
                    max_score = scores[x][y]

        #print("highest_scores:")
        #print(highest_scores)
        #If several same, select one in most middle
        minimum_distance = size*size / 1.0
        best_x = -1
        best_y = -1
        for coords in highest_scores:
            dist = ((coords[0]-size//2)**2 + (coords[1]-size//2)**2)**(1/2)
            if dist < minimum_distance:
                minimum_distance = dist
                best_x = coords[0]
                best_y = coords[1]
                #print("In loop, minimum_dist= " + str(minimum_distance) + " best_x= " + str(best_x) + " best_y= " +str(best_y))
        return (best_x, best_y)





        #turn = (turn+1)%game.number_of_players

