from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from core.game_objects import GameObjects
from core.renderer import Renderer
from views.circle_view import CircleView
from views.null_game_object_view import NullGameObjectView


class GameObjectsManager:
    def __init__(self):
        self.renderer = Renderer(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.game_objects = GameObjects()
        self.view_factories = {}

    def add_object(self, game_object, view_type=None, **kwargs):
        if view_type:
            view_factory = self.view_factories[view_type]
            view = view_factory.create_view(game_object, **kwargs)
            self.renderer.add_object(view)
        else:
            view = NullGameObjectView()

        self.game_objects.add_object(game_object)

    def add_view_factory(self, view_type, view_factory):
        self.view_factories[view_type] = view_factory
