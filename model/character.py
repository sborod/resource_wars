from model.inventory import Inventory
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

    def get_current_tile(self, map):
        return map.get_tile(self.position)

    def loot(self, map):
        current_tile = self.get_current_tile(map)
        items = list(current_tile.inventory.items.items())
        for item, count in items:
            self.inventory.add_item(item, count)
            current_tile.inventory.remove_item(item, count)

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
