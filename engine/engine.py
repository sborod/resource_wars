import pygame
from model.character import Character
from game_objects.character_game_object import CharacterGameObject
from engine.game_objects import GameObjects
from views.game_object_view import GameObjectView

from input_handlers.character_input_handler import CharacterInputHandler
from engine.renderer import Renderer

class Engine:
    def __init__(self, width, height):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.renderer = Renderer(width, height)
        self.game_objects = GameObjects()

        self.input_handler = None

    def handle_quit_event(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def set_input_handler(self, input_handler):
        self.input_handler = input_handler

    def handle_events(self):
        events = pygame.event.get()
        self.handle_quit_event(events)
        if self.input_handler:
            self.input_handler.handle_input(events)

    def update(self):
        self.handle_events()

        # обновление игровых объектов
        self.game_objects.update()
        
    def render(self):
        self.renderer.render()

    def run(self):
        while True:
            self.update()
            self.render()
            self.clock.tick(60)
