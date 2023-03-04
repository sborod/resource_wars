from inventory import Inventory


class Tile:
    def __init__(self, tile_type, resources):
        self.tile_type = tile_type
        self.resources = resources
        self.inventory = Inventory({})

    def add_item(self, item):
        self.inventory.add_item(item)

    def remove_item(self, item):
        self.inventory.remove_item(item)
