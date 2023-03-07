class GameController:
    def __init__(self, game_map):
        self.characters = {}
        self.game_map = game_map
    
    def add_character(self, character):
        self.characters[character.name] = character
