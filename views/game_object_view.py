import pygame

class GameObjectView:
    def __init__(self, game_object, shape, color, size, tile_size):
        self.game_object = game_object
        self.shape = shape
        self.color = color
        self.size = size
        self.tile_size = tile_size

    def render(self, screen):
        pos = self.game_object.get_position()

        if self.shape == "circle":
            radius = self.size // 2
            pygame.draw.circle(screen, self.color, (pos[0]*self.tile_size + radius, pos[1]*self.tile_size + radius), radius)
        elif self.shape == "rectangle":
            pygame.draw.rect(screen, self.color, pygame.Rect(pos[0]*self.tile_size, pos[1]*self.tile_size, self.size, self.size))
