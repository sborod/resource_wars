from core.command import Command


class ShowInventoryCommand(Command):
    def __init__(self, game_controller):
        self.game_controller = game_controller

    def execute(self):
        print("Inventory:", self.game_controller.characters_game_objects["Player"].character.inventory.items)
