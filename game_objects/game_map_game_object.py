from core.game_map import GameMap
from core.game_object_factory import GameObjectFactory
from core.game_object_interface import GameObjectInterface
from model.storage_tile import StorageTile


class GameMapGameObject(GameObjectInterface):
    def __init__(self, width, height):
        self.game_map = GameMap(width, height)

