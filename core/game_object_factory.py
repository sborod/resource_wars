from game_objects.character_game_object import CharacterGameObject
from game_objects.tile_game_object import TileGameObject
from model.character import Character
from model.tile import Tile


class GameObjectFactory:
    @staticmethod
    def create_character_object(name, level, health, max_health, strength, evasion, speed, armor, position):
        character = Character(name, level, health, max_health, strength, evasion, speed, armor, position)
        return CharacterGameObject(character)

    @staticmethod
    def create_tile_object(tile: Tile):
        return TileGameObject(tile)
