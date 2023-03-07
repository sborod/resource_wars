from model.tile import Tile


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[Tile("empty", (i, j)) for j in range(height)] for i in range(width)]

    def get_tile(self, pos):
        x, y = pos
        return self.tiles[x][y]

    def set_tile(self, pos, tile):
        x, y = pos
        self.tiles[x][y] = tile
