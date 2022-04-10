import unittest
from entities.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(10, 5)

    def test_can_add_valid_move(self):
        self.game.add_move(5, 5, 'X')
        self.assertEqual(self.game.board[5][5], 'X')

    def test_cannot_add_move_into_non_empty_square(self):
        self.game.add_move(5, 5, 'X')
        self.assertRaises(ValueError, lambda: self.game.add_move(5, 5, 'Y'))

    def test_cannot_add_move_off_board(self):
        self.assertRaises(
            IndexError, lambda: self.game.add_move(100, 100, 'X'))

    def test_square_location_must_be_integer(self):
        self.assertRaises(TypeError, lambda: self.game.add_move('a', 3, 'X'))
        self.assertRaises(TypeError, lambda: self.game.add_move(3, 'b', 'X'))

    def test_cannot_add_move_if_game_is_over(self):
        self.game.is_over = True
        self.assertRaises(IndexError, lambda: self.game.add_move(5, 5, 'Y'))

    def test_game_is_over_when_board_is_full(self):
        for i in range(100):
            self.game.add_move(int(i % 10), int(i//10), str(i))
        self.assertTrue(self.game.is_over)

    def test_check_when_game_is_won(self):
        self.game.add_move(5, 5, 'X')
        self.game.add_move(1, 0, 'Y')
        self.game.add_move(6, 6, 'X')
        self.game.add_move(5, 3, 'Y')
        self.game.add_move(7, 7, 'X')
        self.game.add_move(2, 8, 'Y')
        self.game.add_move(9, 9, 'X')
        self.game.add_move(1, 4, 'Y')
        self.game.add_move(8, 8, 'X')
        self.assertTrue(self.game.is_won)
