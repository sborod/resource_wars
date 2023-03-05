from core.engine import Engine
from core.game_objects_manager import GameObjectsManager
from core.game_object_factory import GameObjectFactory
from model.storage_tile import StorageTile
from model.tile import Tile
from constants import *
from views.shape_view_factory import ShapeViewFactory


tile_map = [[Tile((i, j), "empty") for j in range(10)] for i in range(10)]
tile_map[5][5] = StorageTile((5, 5), {"gold": 10})

player_game_object = GameObjectFactory.create_character_object("Player", 1, 10, 10, 5, 0, 1, 0, (0, 0))
enemy_game_object = GameObjectFactory.create_character_object("Enemy", 1, 10, 10, 3, 0, 1, 0, (2, 0))

game_objects_manager = GameObjectsManager()
game_objects_manager.add_view_factory("shape", ShapeViewFactory(TILE_SIZE, TILE_SIZE))

for row in tile_map:
    for tile in row:
        if isinstance(tile, StorageTile):
            game_obj = GameObjectFactory.create_tile_object(tile)
            game_objects_manager.add_object(game_obj, view_type="shape", shape="rectangle", color=COLOR_BROWN)

game_objects_manager.add_object(player_game_object, view_type="shape", shape="circle", color=COLOR_BLUE)
game_objects_manager.add_object(enemy_game_object, view_type="shape", shape="circle", color=COLOR_RED)

engine = Engine(game_objects_manager)
engine.set_input_handler(player_game_object.input_handler)

engine.run()
