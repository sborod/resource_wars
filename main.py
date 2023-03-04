from engine.engine import Engine
from game_objects.character_game_object import CharacterGameObject
from model.character import Character
from views.game_object_view import GameObjectView

tile_size = 20
width, height = 800, 600

engine = Engine(width, height)

# создание игровых объектов
player = Character("Player", 1, 10, 10, 5, 0, 1, 0, (0, 0))
enemy = Character("Enemy", 1, 10, 10, 3, 0, 1, 0, (2, 0))

player_game_object = CharacterGameObject(player)
enemy_game_object = CharacterGameObject(enemy)

player_game_object_view = GameObjectView(player_game_object, "circle", (0, 0, 255), tile_size, tile_size)
enemy_game_object_view = GameObjectView(enemy_game_object, "rectangle", (255, 0, 0), tile_size, tile_size)

engine.set_input_handler(player_game_object.input_handler)

engine.game_objects.add_object(player_game_object)
engine.game_objects.add_object(enemy_game_object)

engine.renderer.add_object(player_game_object_view)
engine.renderer.add_object(enemy_game_object_view)

engine.run()
