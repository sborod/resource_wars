import unittest
from game import Game
from inventory import Inventory


class TestInventory(unittest.TestCase):
    
    def setUp(self):
        self.game = Game()
        
    def test_pick_up_loot(self):
        tile = self.game.map.get_tile((1, 1))
        helmet = {"helmet": 1}
        tile.inventory = Inventory(helmet)
        player_character = self.game.player.characters[0]
        player_character.loot(tile)
        self.assertEqual(player_character.inventory.get_item_amount("helmet"), 1)
        self.assertIsNone(tile.inventory)
        
if __name__ == '__main__':
    unittest.main()
