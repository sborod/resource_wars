from views.game_object_view import GameObjectViewInterface


class MenuView(GameObjectViewInterface):
    def __init__(self, menu_game_object):
        self.menu_game_object = menu_game_object

    def render(self, screen):
        if self.menu_game_object.menu.is_enabled():
            self.menu_game_object.menu.draw(screen)
