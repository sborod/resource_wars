import unittest
from model.character import Character
from model.storage_tile import StorageTile
from model.tile import Tile

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character("Bob", 1, 10, 10, 5, 0.2, 2, 1, (0, 0))

    def test_properties(self):
        self.assertEqual(self.character.name, "Bob")
        self.assertEqual(self.character.level, 1)
        self.assertEqual(self.character.health, 10)
        self.assertEqual(self.character.max_health, 10)
        self.assertEqual(self.character.strength, 5)
        self.assertEqual(self.character.evasion, 0.2)
        self.assertEqual(self.character.speed, 2)
        self.assertEqual(self.character.armor, 1)
        self.assertEqual(self.character.position, (0, 0))

    def test_loot_tile_with_inventory(self):
        tile = StorageTile((0, 0), {"gold": 10}, {"helmet": 1})
        self.character.loot(tile)
        self.assertEqual(self.character.inventory.items, {"helmet": 1})

    def test_loot_tile_with_empty_inventory(self):
        tile = Tile((0, 0), "empty")
        self.character.loot(tile)
        self.assertEqual(self.character.inventory.items, {})

    def test_move(self):
        self.character.move((0, 1))
        self.assertEqual(self.character.position, (0, 1))
        self.character.move((1, 1))
        self.assertEqual(self.character.position, (1, 2))

    def test_attack(self):
        enemy = Character("Alice", 1, 10, 10, 3, 0, 1, 0, (1, 0))
        self.character.attack(enemy)
        self.assertEqual(enemy.health, 5)

    def test_attack_with_helmet(self):
            enemy = Character("Alice", 1, 10, 10, 3, 0, 1, 0, (1, 0))
            enemy.inventory.add_item("helmet_1")
            self.character.attack(enemy)
            self.assertEqual(enemy.health, 6)

if __name__ == '__main__':
    unittest.main()
