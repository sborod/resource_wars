from core.engine import Engine
from core.game_controller import GameController
from core.game_objects_manager import GameObjectsManager
from core.game_object_factory import GameObjectFactory
from dialogues import DIALOGUES
from game_objects.NPC_game_object import NPCGameObject
from game_objects.map_game_object import MapGameObject
from game_objects.menu_game_object import MenuGameObject
from input_handlers.input_handler import InputHandler
from model.npc import NPC
from model.storage_tile import StorageTile
from constants import *
from views.menu_view_factory import MenuViewFactory
from views.shape_view_factory import ShapeViewFactory


game_objects_manager = GameObjectsManager()
game_objects_manager.add_view_factory("shape", ShapeViewFactory(TILE_SIZE, TILE_SIZE))
game_objects_manager.add_view_factory("menu", MenuViewFactory())

# create map game object
map_game_object = MapGameObject(10, 10)

# set custom tiles on the map
storage_tile = StorageTile((5, 5), {"gold": 10}, {"helmet": 1})
map_game_object.map.set_tile((5, 5), storage_tile)

# create enemy and player game objects
player_game_object = GameObjectFactory.create_character_object("Player", 1, 10, 10, 5, 0, 1, 0, (0, 0))
enemy_game_object = GameObjectFactory.create_character_object("Enemy", 1, 10, 10, 3, 0, 1, 0, (9, 9))

# add game objects to manager
game_objects_manager.init_tile_objects(map_game_object)
game_objects_manager.add_object(player_game_object, view_type="shape", shape="circle", color=COLOR_BLUE)
game_objects_manager.add_object(enemy_game_object, view_type="shape", shape="circle", color=COLOR_RED)

# create an NPC with a dialogue
john_npc = NPC("John", 1, 10, 10, 3, 0, 1, 0, (2, 2), DIALOGUES["John"])
npc_john_game_object = NPCGameObject(john_npc)

# add the NPC to the game_objects_manager
game_objects_manager.add_object(npc_john_game_object, view_type="shape", shape="circle", color=COLOR_YELLOW)

# init game controller
game_controller = GameController(map_game_object.map, game_objects_manager)

game_controller.add_character(player_game_object)
game_controller.add_character(npc_john_game_object)

# and input handler
input_handler = InputHandler(game_controller)

# init engine
engine = Engine(game_objects_manager)

menu_game_object = MenuGameObject()
game_objects_manager.add_object(menu_game_object, view_type="menu")

engine.set_input_handler(input_handler)

engine.run()
