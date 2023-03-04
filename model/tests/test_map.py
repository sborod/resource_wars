import unittest
from model.character import Character
from model.map import Map
from model.tile import Tile

class TestMap(unittest.TestCase):
    def setUp(self):
        self.map = Map(3, 3)
        tile_data = {
            (0, 0): {"tile_type": "grass", "resources": 1},
            (0, 1): {"tile_type": "water", "resources": 0},
            (0, 2): {"tile_type": "rock", "resources": 2},
            (1, 0): {"tile_type": "grass", "resources": 3},
            (1, 1): {"tile_type": "water", "resources": 0},
            (1, 2): {"tile_type": "rock", "resources": 1},
            (2, 0): {"tile_type": "grass", "resources": 2},
            (2, 1): {"tile_type": "water", "resources": 1},
            (2, 2): {"tile_type": "rock", "resources": 0},
        }
        self.map.generate_map(tile_data)

    def test_generate_map(self):
        self.assertEqual(len(self.map.tiles), 3)
        self.assertEqual(self.map.get_tile((0, 0)).tile_type, Tile("grass", 1).tile_type)
        self.assertEqual(self.map.get_tile((0, 1)).tile_type, Tile("water", 0).tile_type)
        self.assertEqual(self.map.get_tile((0, 2)).tile_type, Tile("rock", 2).tile_type)
        self.assertEqual(self.map.get_tile((1, 0)).tile_type, Tile("grass", 3).tile_type)
        self.assertEqual(self.map.get_tile((1, 1)).tile_type, Tile("water", 0).tile_type)
        self.assertEqual(self.map.get_tile((1, 2)).tile_type, Tile("rock", 1).tile_type)
        self.assertEqual(self.map.get_tile((2, 0)).tile_type, Tile("grass", 2).tile_type)
        self.assertEqual(self.map.get_tile((2, 1)).tile_type, Tile("water", 1).tile_type)
        self.assertEqual(self.map.get_tile((2, 2)).tile_type, Tile("rock", 0).tile_type)

    def test_add_character(self):
        character = Character("Player Character", 1, 10, 10, 1, 0.1, 1, 0, (0, 0))
        self.map.add_character(character)
        self.assertEqual(self.map.characters, [character])
        self.assertEqual(self.map.get_tile((0, 0)).character, character)

    def test_remove_character(self):
        character = Character("Player Character", 1, 10, 10, 1, 0.1, 1, 0, (0, 0))
        self.map.add_character(character)
        self.map.remove_character(character)
        self.assertEqual(self.map.characters, [])
        self.assertEqual(self.map.get_tile((0, 0)).character, None)

    def test_move_character(self):
        character = Character("Player Character", 1, 10, 10, 1, 0.1, 1, 0, (0, 0))
        self.map.add_character(character)
        self.map.move_character(character, (1, 0))
        self.assertEqual(character.position, (1, 0))
        self.assertEqual(self.map.get_tile((0, 0)).character, None)
        self.assertEqual(self.map.get_tile((1, 0)).character, character)

    def test_attack_character(self):
        attacker = Character("Attacker", 1, 10, 10, 1, 0.1, 1, 0, (0, 0))
        defender = Character("Defender", 1, 10, 10, 1, 0.1, 1, 0, (1, 0))
        self.map.add_character(attacker)
        self.map.add_character(defender)
        self.assertTrue(self.map.attack(attacker, defender))
        self.assertEqual(defender.health, 9)

    # def test_pickup_from_inventory(self):
    #     # Arrange
    #     map_size = 3
    #     game_map = Map(map_size)
    #     character = Character("player", 100, 10, 5)
    #     game = Game(game_map, character)
    #     helmet = {"name": "helmet", "defense": 5}
    #     inventory = Inventory(helmet)
    #     game.map.get_tile((1, 1)).inventory = inventory
        
    #     # Act
    #     game.character.move("down")  # move to tile with inventory
    #     game.character.pick_up()
        
    #     # Assert
    #     self.assertTrue("helmet" in game.character.inventory.items)
