from model.map import Map
from core.game_object_factory import GameObjectFactory
from core.game_object_interface import GameObjectInterface
from model.storage_tile import StorageTile


class MapGameObject(GameObjectInterface):
    def __init__(self, width, height):
        self.game_map = Map(width, height)

