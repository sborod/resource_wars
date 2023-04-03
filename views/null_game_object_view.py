from views.game_object_view import GameObjectViewInterface


class NullGameObjectView(GameObjectViewInterface):
    def render(self, screen):
        pass
