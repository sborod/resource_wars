from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from core.game_objects import GameObjects
from core.renderer import Renderer
from views.shape_view import ShapeView
from views.null_game_object_view import NullGameObjectView


class GameObjectsManager:
    def __init__(self):
        self.renderer = Renderer(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.game_objects = GameObjects()

    def add_object(self, game_object, shape=None, color=None, size=None, tile_size=None):
        if shape and color and size and tile_size:
            view = ShapeView(game_object, shape, color, size, tile_size)
            self.renderer.add_object(view)
        else:
            view = NullGameObjectView()

        self.game_objects.add_object(game_object)
