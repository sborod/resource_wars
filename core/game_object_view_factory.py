from abc import ABC, abstractmethod
from typing import TypeVar

from core.game_object_interface import GameObjectInterface
from views.game_object_view import GameObjectViewInterface

GameObjectType = TypeVar("GameObjectType", bound=GameObjectInterface)
ViewType = TypeVar("ViewType", bound=GameObjectViewInterface)

class GameObjectViewFactory(ABC):
    @abstractmethod
    def create_view(self, game_object):
        pass
