from core.game_object_interface import GameObjectInterface
from input_handlers.character_input_handler import CharacterInputHandler

class CharacterGameObject(GameObjectInterface):
    def __init__(self, character):
        self.character = character
        self.input_handler = CharacterInputHandler(character)

    def get_position(self):
        return self.character.position
    