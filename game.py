import random
from inventory import Inventory
from map import Map
from character import Character
from player import Player

class Game:
    def __init__(self):
        self.map = Map(3, 3)
        initial_tile_data = {
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
        self.map.generate_map(initial_tile_data)
        self.player = Player()
        character = Character("Player Character 1", 1, 10, 10, 1, 0.1, 1, 0, (0, 0))
        self.player.characters.append(character)

    def add_enemies(self, number_of_enemies):
        for i in range(number_of_enemies):
            name = f"Enemy {i+1}"
            level = 1
            health = random.randint(50, 100)
            max_health = health
            strength = random.randint(5, 10)
            evasion = random.uniform(0, 0.3)
            speed = random.randint(1, 2)
            armor = random.randint(0, 2)
            position = (random.randint(0, 2), random.randint(0, 2))
            enemy = Character(name, level, health, max_health, strength, evasion, speed, armor, position)
            self.map.add_character(enemy)

    def start(self):
        self.map.add_character(self.player.characters[0])
        self.add_enemies(3)
