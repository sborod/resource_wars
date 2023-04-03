from core.game_object_view_factory import GameObjectViewFactory
from views.menu_view import MenuView


class MenuViewFactory(GameObjectViewFactory):
    def create_view(self, game_object):
        return MenuView(game_object)
