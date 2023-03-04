# класс, представляющий игровой объект
from game_object_interface import GameObjectInterface


class GameObject(GameObjectInterface):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def update(self):
        pass

    def get_position(self):
        return self.position
