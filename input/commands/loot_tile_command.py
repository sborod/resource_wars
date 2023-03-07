from core.command import Command


class LootTileCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        self.game_controller.characters_game_objects["Player"].character.loot(self.game_controller.map)
