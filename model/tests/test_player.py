import unittest
from model.player import Player

class TestPlayer(unittest.TestCase):
    def test_player_creation(self):
        player = Player("John", 1000)
        self.assertEqual(player.name, "John")
        self.assertEqual(player.money, 1000)
        self.assertEqual(player.characters, [])
        self.assertEqual(player.units, [])
        self.assertEqual(player.owned_tiles, [])
        self.assertEqual(player.experience, 0)
        self.assertEqual(player.level, 1)
