from abc import ABC, abstractmethod

class GameObjectViewFactory(ABC):
    @abstractmethod
    def create_view(self, game_object):
        pass
