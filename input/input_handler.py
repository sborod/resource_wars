from typing import List
import pygame
from core.game_controller import GameController

from core.input_handler_interface import InputHandlerInterface
from input.commands.interact_with_npc_command import InteractWithNPCCommand
from input.commands.loot_tile_command import LootTileCommand
from input.commands.move_down_command import MoveDownCommand
from input.commands.move_left_command import MoveLeftCommand
from input.commands.move_right_command import MoveRightCommand
from input.commands.move_up_command import MoveUpCommand
from input.commands.show_inventory_command import ShowInventoryCommand
from input.commands.show_tile_loot_command import ShowTileLootCommand


class InputHandler(InputHandlerInterface):
    def __init__(self, game_controller: GameController):
        self.game_controller = game_controller
        self.keymap = {
            pygame.K_UP: MoveUpCommand,
            pygame.K_DOWN: MoveDownCommand,
            pygame.K_LEFT: MoveLeftCommand,
            pygame.K_RIGHT: MoveRightCommand,
            pygame.K_SPACE: LootTileCommand,
            pygame.K_i: ShowInventoryCommand,
            pygame.K_TAB: ShowTileLootCommand,
            pygame.K_q: InteractWithNPCCommand,
        }

    def handle_input(self, events: List[pygame.event.Event]):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in self.keymap:
                    command = self.keymap[event.key](self.game_controller)
                    command.execute()
