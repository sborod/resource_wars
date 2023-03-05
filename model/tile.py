from model.inventory import Inventory

class Tile:
    def __init__(self, tile_type, position, resources={}, inventory={}):
        self.tile_type = tile_type
        self.position = position
        self.resources = resources
        self.inventory = Inventory(inventory)

    def add_item(self, item_name, amount=1):
        self.inventory.add_item(item_name, amount)

    def remove_item(self, item):
        self.inventory.remove_item(item)
