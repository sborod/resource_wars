from abc import ABC, abstractmethod

class GameObjectViewInterface(ABC):
    @abstractmethod
    def render(self, screen):
        pass
