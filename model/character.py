from model.inventory import Inventory
from model.tile import Tile
from model.item_stats import ITEM_STATS

class Character:
    def __init__(self, name, level, health, max_health, strength, evasion, speed, armor, position):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.strength = strength
        self.evasion = evasion
        self.speed = speed
        self.armor = armor
        self.position = position
        self.inventory = Inventory({})

    def loot(self, tile):
        if isinstance(tile, Tile) and tile.inventory is not None:
            for item, count in tile.inventory.items.items():
                if item in self.inventory.items:
                    self.inventory.items[item] += count
                else:
                    self.inventory.items[item] = count
            tile.inventory = None
            return True
        return False

    def move(self, delta_position):
        """Move character by delta (dx, dy) on the map."""
        x, y = self.position
        delta_x, delta_y = delta_position
        new_x, new_y = x + delta_x, y + delta_y
        self.position = (new_x, new_y)
        
    def attack(self, target):
        total_armor = target.armor
        for item, count in target.inventory.items.items():
            item_stats = ITEM_STATS.get(item)
            if item_stats and "armor" in item_stats:
                total_armor += item_stats["armor"] * count
        damage = self.strength - total_armor
        if damage > 0:
            target.health -= damage
            if target.health < 0:
                target.health = 0
            return True
        else:
            return False