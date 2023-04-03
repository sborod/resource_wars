import pygame

from views.game_object_view import GameObjectViewInterface

class CircleView(GameObjectViewInterface):
    def __init__(self, game_object, color, size, tile_size):
        self.game_object = game_object
        self.color = color
        self.size = size
        self.tile_size = tile_size

    def get_position(self):
        return self.game_object.get_position()

    def render(self, screen):
        pos = self.get_position()
        if pos is not None:
            radius = self.size // 2
            pygame.draw.circle(screen, self.color, (pos[0]*self.tile_size + radius, pos[1]*self.tile_size + radius), radius)
