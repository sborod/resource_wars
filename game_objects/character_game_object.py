from core.game_object_interface import GameObjectInterface

class CharacterGameObject(GameObjectInterface):
    def __init__(self, character):
        self.character = character

    def get_position(self):
        return self.character.position
    