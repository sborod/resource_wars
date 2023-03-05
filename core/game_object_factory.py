from game_objects.character_game_object import CharacterGameObject
from game_objects.tile_game_object import TileGameObject
from game_objects.tile_map_game_object import TileMapGameObject
from model.character import Character


class GameObjectFactory:
    @staticmethod
    def create_character_object(name, level, health, max_health, strength, evasion, speed, armor, position):
        character = Character(name, level, health, max_health, strength, evasion, speed, armor, position)
        return CharacterGameObject(character)

    @staticmethod
    def create_tile_object(tile):
        return TileGameObject(tile)

    @staticmethod
    def create_tile_map_object(tile_map):
        return TileMapGameObject(tile_map)
