from core.engine import Engine
from core.game_controller import GameController
from core.game_objects_manager import GameObjectsManager
from core.game_object_factory import GameObjectFactory
from game_objects.game_map_game_object import GameMapGameObject
from input_handlers.input_handler import InputHandler
from model.storage_tile import StorageTile
from constants import *
from views.shape_view_factory import ShapeViewFactory


game_objects_manager = GameObjectsManager()
game_objects_manager.add_view_factory("shape", ShapeViewFactory(TILE_SIZE, TILE_SIZE))

game_map_game_object = GameMapGameObject(10, 10)
storage_tile = StorageTile((5, 5), {"gold": 10}, {"helmet": 1})
game_map_game_object.game_map.set_tile((5, 5), storage_tile)

player_game_object = GameObjectFactory.create_character_object("Player", 1, 10, 10, 5, 0, 1, 0, (0, 0))
enemy_game_object = GameObjectFactory.create_character_object("Enemy", 1, 10, 10, 3, 0, 1, 0, (2, 0))

game_objects_manager.init_tile_objects(game_map_game_object)
game_objects_manager.add_object(player_game_object, view_type="shape", shape="circle", color=COLOR_BLUE)
game_objects_manager.add_object(enemy_game_object, view_type="shape", shape="circle", color=COLOR_RED)

game_controller = GameController(player_game_object.character, game_map_game_object.game_map)
input_handler = InputHandler(game_controller)

engine = Engine(game_objects_manager)
engine.set_input_handler(input_handler)

engine.run()
