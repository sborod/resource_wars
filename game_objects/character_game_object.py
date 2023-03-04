from engine.game_object_interface import GameObjectInterface

# адаптер, преобразующий персонажа в игровой объект
class CharacterGameObject(GameObjectInterface):
    def __init__(self, character):
        self.character = character

    def get_position(self):
        return self.character.position
    