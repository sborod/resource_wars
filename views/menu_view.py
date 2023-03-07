from views.game_object_view import GameObjectView


class MenuView(GameObjectView):
    def __init__(self, menu_game_object):
        self.menu_game_object = menu_game_object

    def render(self, screen):
        if self.menu_game_object.menu.is_enabled():
            self.menu_game_object.menu.draw(screen)
