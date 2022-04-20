import unittest
from services.game_service import GameService


class MockplayerScoreRepository:
    def __init__(self, scores=None):
        self.scores = scores or []


    def add_player(self, name):
        for score in self.scores:
            if score[0] == name:
                return
        self.scores.append([name,0,0,0])

    def get_names(self):
        names = []
        for score in self.scores:
            names.append(score[0])
        return names

    def get_scores(self):
        scores = []
        for score in self.scores:
            scores.append(score)
        return scores

    def update_score(self, name, win, loss, draw):
        index = -1
        for i in range(len(self.scores)):
            if self.scores[i][0] == name:
                index = i

        if index < 0:
            return False
        
        self.scores[index][1] += win
        self.scores[index][2] += loss
        self.scores[index][3] += draw
        
        return True



class TestGameService(unittest.TestCase):
    def setUp(self):
        self.service= GameService(MockplayerScoreRepository())
        self.service.new_game(3, 3)
        self.service.add_player('Test1', 'X', 'Human', 0, True)
        self.service.add_player('Test2', 'O', 'Human', 100, True)

    def test_can_add_player(self):
        self.service.add_player('Robot1', '+', 'Valuebased', 100, False)
        self.assertEqual(self.service.number_of_players, 3)

    def test_can_start_new_game(self):
        self.service.new_game(10, 5)
        self.assertEqual(self.service.number_of_players, 0)

    def test_game_is_over(self):
        self.service.add_move_and_get_updates(0)
        self.service.add_move_and_get_updates(2)
        self.service.add_move_and_get_updates(1)
        self.service.add_move_and_get_updates(3)
        self.service.add_move_and_get_updates(5)
        self.service.add_move_and_get_updates(4)
        self.service.add_move_and_get_updates(8)
        self.service.add_move_and_get_updates(7)
        self.service.add_move_and_get_updates(6)
        self.assertTrue(self.service.game_is_over)

    def test_game_is_won(self):
        for i in range(3):
            self.service.add_move_and_get_updates(i)
            self.service.add_move_and_get_updates(i+5)

        self.assertTrue(self.service.game_is_won)

    def test_computer_makes_moves(self):
        self.service.new_game(3, 3)
        self.service.add_player('Robot1', 'X', 'Valuebased', 100, False)
        self.service.add_player('Test1', 'O', 'Human', 0, True)
        self.service.make_computer_moves_and_get_updates()
        self.service.add_move_and_get_updates(2)
        self.service.add_move_and_get_updates(7)
        self.service.add_move_and_get_updates(0)
        self.service.add_move_and_get_updates(5)
        self.assertTrue(self.service.game_is_over)

    def test_can_find_winning_row(self):
        self.service.add_move_and_get_updates(0)
        self.service.add_move_and_get_updates(3)
        self.service.add_move_and_get_updates(1)
        self.service.add_move_and_get_updates(4)
        self.service.add_move_and_get_updates(2)
        self.assertEqual(self.service.get_winning_row(), [2, 1, 0])

    def test_can_retrieve_scores(self):
        self.service= GameService(MockplayerScoreRepository())
        self.service.new_game(3, 1)
        self.service.add_player('Test1', 'X', 'Human', 0, True)
        self.service.add_player('Test2', 'O', 'Valuebased', 100, False)
        self.service.add_move_and_get_updates(0)
        scores = self.service.get_scores()
        self.assertEqual(scores[0][1], 1)

    def test_can_retrieve_players(self):
        self.assertEqual(len(self.service.get_all_players_from_db()), 2)

    def test_can_retrieve_algorithms(self):
        self.assertEqual(len(self.service.get_algorithms()), 3)

    def test_get_winner_symbol(self):
        self.service= GameService(MockplayerScoreRepository())
        self.service.new_game(3, 1)
        self.service.add_player('Test1', 'X', 'Human', 0, True)
        self.service.add_player('Test2', 'O', 'Valuebased', 100, False)
        self.service.add_move_and_get_updates(0)
        self.assertEqual(self.service.winner_symbol, 'X')

    def test_get_winner_symbol_when_game_not_won(self):
        winner_symbol = self.service.winner_symbol
        self.assertEqual(len(winner_symbol), 0)

    def test_get_turn_symbol(self):
        self.service= GameService(MockplayerScoreRepository())
        self.service.new_game(3, 3)
        self.service.add_player('Test1', 'X', 'Human', 0, True)
        self.service.add_player('Test2', 'O', 'Uniform', 100, False)
        self.service.add_move_and_get_updates(0)
        self.assertEqual(self.service.turn_symbol, 'X')

    def test_get_turn_symbol_when_game_is_over(self):
        self.service= GameService(MockplayerScoreRepository())
        self.service.new_game(3, 1)
        self.service.add_player('Test1', 'X', 'Human', 0, True)
        self.service.add_player('Test2', 'O', 'Valuebased', 100, False)
        self.service.add_move_and_get_updates(0)
        turn_symbol = self.service.turn_symbol
        self.assertEqual(len(turn_symbol), 0)

    def test_get_board(self):
        self.assertTrue(self.service.board)

    def test_cannot_require_more_to_win_than_fits_board(self):
        self.assertRaises(ValueError, lambda: self.service.new_game(3, 7))
