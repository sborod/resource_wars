import pygame

from core.input_handler_interface import InputHandlerInterface

class Command:
    def execute(self):
        pass

class MoveUpCommand(Command):
    def __init__(self, character):
        self.character = character

    def execute(self):
        self.character.move((0, -1))

class MoveDownCommand(Command):
    def __init__(self, character):
        self.character = character

    def execute(self):
        self.character.move((0, 1))

class MoveLeftCommand(Command):
    def __init__(self, character):
        self.character = character

    def execute(self):
        self.character.move((-1, 0))

class MoveRightCommand(Command):
    def __init__(self, character):
        self.character = character

    def execute(self):
        self.character.move((1, 0))

class InteractWithStorageCommand(Command):
    def __init__(self, character, tile):
        self.character = character
        self.tile = tile

    def execute(self):
        if self.tile.tile_type == 'storage':
            self.character.loot(self.tile.inventory)

class CharacterInputHandler(InputHandlerInterface):
    def __init__(self, character):
        self.character = character
        self.keymap = {
            pygame.K_UP: MoveUpCommand,
            pygame.K_DOWN: MoveDownCommand,
            pygame.K_LEFT: MoveLeftCommand,
            pygame.K_RIGHT: MoveRightCommand,
        }

    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in self.keymap:
                    command = self.keymap[event.key](self.character)
                    command.execute()
