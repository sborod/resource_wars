import pygame_menu
from views.game_object_view import GameObjectView


class MenuView(GameObjectView):
    def __init__(self):
        self.menu = pygame_menu.Menu(
            width=400,
            height=400,
            theme=pygame_menu.themes.THEME_DEFAULT,
            title="Hello"
        )

    def render(self, screen):
        self.menu.draw(screen)

