from model.tile import Tile

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.characters = []
        self.tiles = [[None for x in range(width)] for y in range(height)]

    def generate_map(self, tile_data):
        for x in range(self.width):
            for y in range(self.height):
                tile_type = tile_data[(x, y)]["tile_type"]
                resources = tile_data[(x, y)]["resources"]
                self.tiles[x][y] = Tile(tile_type, resources)

    def add_inventory(self, tile, inventory):
        tile.inventory = inventory

    def add_character(self, character):
        self.characters.append(character)
        x, y = character.position
        self.tiles[x][y].character = character

    def remove_character(self, character):
        self.characters.remove(character)
        x, y = character.position
        self.tiles[x][y].character = None

    def get_tile(self, pos):
        x, y = pos
        return self.tiles[x][y]

    def attack(self, attacker, target):
        """Attacks the target with the attacker's strength."""
        return attacker.attack(target)

    def move_character(self, character, delta):
        """Moves the character by delta."""
        x, y = character.position
        delta_x, delta_y = delta
        new_x, new_y = x + delta_x, y + delta_y
        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            character.move(delta)
            self.tiles[x][y].character = None
            self.tiles[new_x][new_y].character = character
            return True
        else:
            return False
