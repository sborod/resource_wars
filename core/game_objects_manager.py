from constants import COLOR_BROWN, COLOR_GREEN, SCREEN_HEIGHT, SCREEN_WIDTH
from core.game_object_factory import GameObjectFactory
from core.game_objects import GameObjects
from core.renderer import Renderer
from model.storage_tile import StorageTile
from views.null_game_object_view import NullGameObjectView


class GameObjectsManager:
    def __init__(self):
        self.renderer = Renderer(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.game_objects = GameObjects()
        self.view_factories = {}

    def add_object(self, game_object, view_type=None, **kwargs):
        if view_type:
            view_factory = self.view_factories[view_type]
            view = view_factory.create_view(game_object, **kwargs)
            self.renderer.add_object(view)
        else:
            view = NullGameObjectView()

        self.game_objects.add_object(game_object)

    def add_view_factory(self, view_type, view_factory):
        self.view_factories[view_type] = view_factory

    def init_tile_objects(self, map_game_object):
        game_objects = []
        for i, row in enumerate(map_game_object.map.tiles):
            for j, tile in enumerate(row):
                game_obj = GameObjectFactory.create_tile_object(tile)
                game_objects.append(game_obj)
        for tile_game_object in game_objects:
            if tile_game_object.tile.tile_type == "empty":
                self.add_object(tile_game_object, view_type="shape", shape="rectangle", color=COLOR_GREEN)
            elif tile_game_object.tile.tile_type == "storage":
                self.add_object(tile_game_object, view_type="shape", shape="rectangle", color=COLOR_BROWN)
