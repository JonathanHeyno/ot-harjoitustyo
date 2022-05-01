import unittest
#from database_connection import get_database_connection
from repositories.player_scores_repository import score_repository




class PlayerScoresRepository(unittest.TestCase):
    def setUp(self):
        score_repository.delete_all()
        score_repository.add_player("Bill Gates")
        score_repository.add_player("Steve Jobs")
        score_repository.update_score("Bill Gates", 3, 1, 6)
        score_repository.update_score("Steve Jobs", 1, 7, 100)
    
    def test_add_player(self):
        score_repository.add_player("Dracula")
        self.assertEqual(len(score_repository.get_names()), 3)

    def test_add_empty_player(self):
        score_repository.add_player("")
        self.assertEqual(len(score_repository.get_names()), 2)

    def test_add_existing_player(self):
        score_repository.add_player("Bill Gates")
        self.assertEqual(len(score_repository.get_names()), 2)

    def test_get_names(self):
        self.assertEqual(len(score_repository.get_names()), 2)

    def test_get_scores(self):
        scores = score_repository.get_scores()
        self.assertEqual(scores[0][0], "Bill Gates")
        self.assertEqual(scores[0][1], 3)
        self.assertEqual(scores[0][2], 1)
        self.assertEqual(scores[0][3], 6)
        self.assertEqual(scores[1][0], "Steve Jobs")
        self.assertEqual(scores[1][1], 1)
        self.assertEqual(scores[1][2], 7)
        self.assertEqual(scores[1][3], 100)

    def test_update_score(self):
        score_repository.update_score("Steve Jobs", 8, 9, 10)
        scores = score_repository.get_scores()
        self.assertEqual(scores[1][0], "Steve Jobs")
        self.assertEqual(scores[1][1], 9)
        self.assertEqual(scores[1][2], 16)
        self.assertEqual(scores[1][3], 110)

    def test_update_score_for_no_named_player(self):
        result = score_repository.update_score("", 8, 9, 10)
        self.assertFalse(result)

    def test_delete_all(self):
        score_repository.delete_all()
        scores = score_repository.get_scores()
        self.assertEqual(len(score_repository.get_names()), 0)
