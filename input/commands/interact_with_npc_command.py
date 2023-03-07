import pygame_menu
from core.command import Command


class InteractWithNPCCommand(Command):
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
                    submenu.add.label(response)
                submenu.add.button("Next", submenu.disable)
                self.game_controller.menu_game_object.menu.add.button(option, submenu)
            else:
                for response in dialogue[option]["response"].split("\n"):
                    self.game_controller.menu_game_object.menu.add.label(response)
        self.game_controller.menu_game_object.menu.toggle()
        self.game_controller.menu_game_object.menu.force_surface_cache_update()
