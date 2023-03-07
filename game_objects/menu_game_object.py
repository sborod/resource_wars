import pygame_menu
from core.game_object_interface import GameObjectInterface

class MenuGameObject(GameObjectInterface):
    def __init__(self):
        self.menu = pygame_menu.Menu(
            width=400,
            height=400,
            theme=pygame_menu.themes.THEME_DEFAULT,
            title="Hello"
        )
        self.menu.disable()
    
    def update(self, events):
        if self.menu.is_enabled():
            self.menu.update(events)
