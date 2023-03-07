class GameController:
    def __init__(self, map):
        self.characters = {}
        self.map = map
    
    def add_character(self, character):
        self.characters[character.name] = character
