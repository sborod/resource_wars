import unittest
from model.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_start_game(self):
        self.game.start()
        self.assertEqual(len(self.game.map.characters), 4)
