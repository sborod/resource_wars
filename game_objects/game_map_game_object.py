from core.game_object_factory import GameObjectFactory
from core.game_object_interface import GameObjectInterface
from model.storage_tile import StorageTile


class GameMapGameObject(GameObjectInterface):
    def __init__(self, tile_map):
        self.tile_map = tile_map
        self.game_objects = []

    def create_game_objects(self):
        for i, row in enumerate(self.tile_map):
            for j, tile in enumerate(row):
                if isinstance(tile, StorageTile):
                    game_obj = GameObjectFactory.create_tile_object(tile)
                    self.game_objects.append(game_obj)

    def get_tile(self, x, y):
        return self.tile_map[x][y]

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)

    def remove_game_object(self, game_object):
        self.game_objects.remove(game_object)

    def get_game_objects(self):
        return self.game_objects
