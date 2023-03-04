import unittest
from tile import Tile

class TestTile(unittest.TestCase):
    def test_new_tile(self):
        tile = Tile("forest", {'wood': 10, 'stone': 5})
        self.assertEqual(tile.tile_type, "forest")
        self.assertEqual(tile.resources["wood"], 10)
        self.assertEqual(tile.resources["stone"], 5)

if __name__ == '__main__':
    unittest.main()
