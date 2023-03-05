from abc import ABC, abstractmethod

class GameObjectView(ABC):
    @abstractmethod
    def render(self, screen):
        pass
