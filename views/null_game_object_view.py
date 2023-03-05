from views.game_object_view import GameObjectView


class NullGameObjectView(GameObjectView):
    def render(self, screen):
        pass
