from core.game_object_interface import GameObjectInterface


class TileGameObject(GameObjectInterface):
    def __init__(self, tile):
        self.tile = tile

    def get_position(self):
        return self.tile.position
