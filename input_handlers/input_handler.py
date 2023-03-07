import pygame
import pygame_menu
from constants import FONT_NAME
from core.command import Command

from core.input_handler_interface import InputHandlerInterface
from model.storage_tile import StorageTile

class MoveUpCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        self.game_controller.characters_game_objects["Player"].character.move((0, -1))

class MoveDownCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        self.game_controller.characters_game_objects["Player"].character.move((0, 1))

class MoveLeftCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        self.game_controller.characters_game_objects["Player"].character.move((-1, 0))

class MoveRightCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        self.game_controller.characters_game_objects["Player"].character.move((1, 0))

class LootTileCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        self.game_controller.characters_game_objects["Player"].character.loot(self.game_controller.map)

class ShowInventoryCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        print("Inventory:", self.game_controller.characters_game_objects["Player"].character.inventory.items)

class ShowTileLootCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        current_tile = self.game_controller.characters_game_objects["Player"].character.get_current_tile(self.game_controller.map)
        if isinstance(current_tile, StorageTile):
            print("Tile loot:", current_tile.inventory.items)
        else:
            print("There is no loot on the current tile")

class InteractWithNPC(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        dialogue = self.game_controller.characters_game_objects["John"].character.dialogue
        print(dialogue)
        for option in dialogue.keys():
            if not dialogue[option]["end"]:
                submenu = pygame_menu.Menu(
                    width=400,
                    height=400,
                    theme=pygame_menu.themes.THEME_DEFAULT,
                    title=option
                )
                for response in dialogue[option]["response"].split("\n"):
                    submenu.add.label(response, font_size=20, font_name=FONT_NAME)
                submenu.add.button("Next", submenu.disable)
                self.game_controller.menu_game_object.menu.add.button(option, submenu)
            else:
                for response in dialogue[option]["response"].split("\n"):
                    self.game_controller.menu_game_object.menu.add.label(response)
        self.game_controller.menu_game_object.menu.toggle()
        self.game_controller.menu_game_object.menu.force_surface_cache_update()

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
