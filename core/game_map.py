class GameMap:
    def __init__(self, tile_map):
        self.tiles = tile_map

    def get_tile(self, position):
        x, y = position
        if x < 0 or x >= len(self.tiles) or y < 0 or y >= len(self.tiles[x]):
            return None
        return self.tiles[x][y]
