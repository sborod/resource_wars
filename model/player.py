class Player:
    def __init__(self, name="Player", starting_money=600):
        self.name = name
        self.money = starting_money
        self.characters = []
        self.units = []
        self.owned_tiles = []
        self.experience = 0
        self.level = 1

    def attack_tile(self, tile):
        pass  # реализация атаки клетки

    def move_character(self, character, tile):
        pass  # реализация движения персонажа на клетку

    def move_unit(self, unit, tile):
        pass  # реализация движения юнита на клетку