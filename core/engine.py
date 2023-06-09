import sys
from typing import List
import pygame

from core.game_objects_manager import GameObjectsManager
from input.input_handler import InputHandler

class Engine:
    def __init__(self, game_objects_manager: GameObjectsManager):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.game_objects_manager = game_objects_manager
        self.input_handler = None

    def handle_quit_event(self, events: List[pygame.event.Event]):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def set_input_handler(self, input_handler: InputHandler):
        self.input_handler = input_handler

    def handle_events(self):
        events = pygame.event.get()
        self.handle_quit_event(events)
        if self.input_handler:
            self.input_handler.handle_input(events)
        return events

    def update(self):
        events = self.handle_events()
        self.game_objects_manager.game_objects.update(events)
        
    def render(self):
        self.game_objects_manager.renderer.render()

    def run(self):
        while True:
            self.update()
            self.render()
            self.clock.tick(60)
