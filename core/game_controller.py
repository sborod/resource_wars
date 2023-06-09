from core.game_objects_manager import GameObjectsManager
from model.map import Map


class GameController:
    def __init__(self, map: Map, game_objects_manager: GameObjectsManager):
        self.characters_game_objects = {}
        self.map = map
        self.game_objects_manager = game_objects_manager
        self.menu_game_object = None
    
    def add_character(self, character_game_object):
        self.characters_game_objects[character_game_object.character.name] = character_game_object

    def set_menu_game_object(self, menu_game_object):
        self.menu_game_object = menu_game_object
