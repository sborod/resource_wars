from core.command import Command
from model.storage_tile import StorageTile


class ShowTileLootCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        current_tile = self.game_controller.characters_game_objects["Player"].character.get_current_tile(self.game_controller.map)
        if isinstance(current_tile, StorageTile):
            print("Tile loot:", current_tile.inventory.items)
        else:
            print("There is no loot on the current tile")
