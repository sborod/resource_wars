from core.game_object_interface import GameObjectInterface


class TileMapGameObject(GameObjectInterface):
    def __init__(self, tile_map):
        self.tile_map = tile_map
