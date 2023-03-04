import pygame

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

class PygameInputHandler:
    def __init__(self, game_object):
        self.game_object = game_object
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
                    command = self.keymap[event.key](self.game_object.character)
                    command.execute()
