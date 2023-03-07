import pygame
from core.command import Command

from core.input_handler_interface import InputHandlerInterface
from model.storage_tile import StorageTile

class MoveUpCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        self.game_controller.characters["Player"].move((0, -1))

class MoveDownCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        self.game_controller.characters["Player"].move((0, 1))

class MoveLeftCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        self.game_controller.characters["Player"].move((-1, 0))

class MoveRightCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        self.game_controller.characters["Player"].move((1, 0))

class LootTileCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        self.game_controller.characters["Player"].loot(self.game_controller.game_map)

class ShowInventoryCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        print("Inventory:", self.game_controller.characters["Player"].inventory.items)

class ShowTileLootCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        current_tile = self.game_controller.characters["Player"].get_current_tile(self.game_controller.game_map)
        if isinstance(current_tile, StorageTile):
            print("Tile loot:", current_tile.inventory.items)
        else:
            print("There is no loot on the current tile")

class InteractWithNPC(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        print("John.dialogue:", self.game_controller.characters["John"].dialogue)

class InputHandler(InputHandlerInterface):
    def __init__(self, game_controller):
        self.game_controller = game_controller
        self.keymap = {
            pygame.K_UP: MoveUpCommand,
            pygame.K_DOWN: MoveDownCommand,
            pygame.K_LEFT: MoveLeftCommand,
            pygame.K_RIGHT: MoveRightCommand,
            pygame.K_SPACE: LootTileCommand,
            pygame.K_i: ShowInventoryCommand,
            pygame.K_TAB: ShowTileLootCommand,
            pygame.K_q: InteractWithNPC,
        }

    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in self.keymap:
                    command = self.keymap[event.key](self.game_controller)
                    command.execute()
