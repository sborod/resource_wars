from views.circle_view import CircleView
from views.null_game_object_view import NullGameObjectView
from views.rectangle_view import RectangleView


class ShapeViewFactory:
    def __init__(self, size, tile_size):
        self.size = size
        self.tile_size = tile_size

    def create_view(self, game_object, shape, color):
        if shape == "circle":
            return CircleView(game_object, color, self.size, self.tile_size)
        elif shape == "rectangle":
            return RectangleView(game_object, color, self.size, self.tile_size)
        else:
            return NullGameObjectView()
