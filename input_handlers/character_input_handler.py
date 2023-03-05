import pygame
from core.command import Command

from core.input_handler_interface import InputHandlerInterface
from model.storage_tile import StorageTile

class MoveUpCommand(Command):
    def __init__(self, character, game_map):
        self.character = character

    def execute(self):
        self.character.move((0, -1))

class MoveDownCommand(Command):
    def __init__(self, character, game_map):
        self.character = character

    def execute(self):
        self.character.move((0, 1))

class MoveLeftCommand(Command):
    def __init__(self, character, game_map):
        self.character = character

    def execute(self):
        self.character.move((-1, 0))

class MoveRightCommand(Command):
    def __init__(self, character, game_map):
        self.character = character

    def execute(self):
        self.character.move((1, 0))

class LootTileCommand(Command):
    def __init__(self, character, game_map):
        self.character = character
        self.game_map = game_map

    def execute(self):
        self.character.loot(self.game_map)

class ShowInventoryCommand(Command):
    def __init__(self, character, game_map):
        self.character = character

    def execute(self):
        print("Inventory:", self.character.inventory.items)

class ShowTileLootCommand(Command):
    def __init__(self, character, game_map):
        self.character = character
        self.game_map = game_map

    def execute(self):
        current_tile = self.character.get_current_tile(self.game_map)
        if isinstance(current_tile, StorageTile):
            print("Tile loot:", current_tile.inventory.items)
        else:
            print("There is no loot on the current tile")

class CharacterInputHandler(InputHandlerInterface):
    def __init__(self, character):
        self.character = character
        self.keymap = {
            pygame.K_UP: MoveUpCommand,
            pygame.K_DOWN: MoveDownCommand,
            pygame.K_LEFT: MoveLeftCommand,
            pygame.K_RIGHT: MoveRightCommand,
            pygame.K_SPACE: LootTileCommand,
            pygame.K_i: ShowInventoryCommand,
            pygame.K_TAB: ShowTileLootCommand,
        }

    def handle_input(self, events, game_map):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in self.keymap:
                    command = self.keymap[event.key](self.character, game_map)
                    command.execute()
