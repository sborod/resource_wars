from model.tile import Tile


class StorageTile(Tile):
    def __init__(self, position, resources={}, inventory={}):
        super().__init__('storage', position, resources, inventory)
