import pygame
from model.character import Character
from game_objects.character_game_object import CharacterGameObject
from engine.game_logic import GameLogic
from views.game_object_view import GameObjectView

from input_handlers.character_input_handler import CharacterInputHandler
from engine.renderer import Renderer

tile_size = 20

class PygameGame:
    def __init__(self, width, height):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.renderer = Renderer(width, height)
        self.game_logic = GameLogic()

        # создание игровых объектов
        player = Character("Player", 1, 10, 10, 5, 0, 1, 0, (0, 0))
        enemy = Character("Enemy", 1, 10, 10, 3, 0, 1, 0, (2, 0))

        player_game_object = CharacterGameObject(player)
        enemy_game_object = CharacterGameObject(enemy)

        player_game_object_view = GameObjectView(player_game_object, "circle", (0, 0, 255), tile_size, tile_size)
        enemy_game_object_view = GameObjectView(enemy_game_object, "rectangle", (255, 0, 0), tile_size, tile_size)

        self.set_input_handler(player_game_object.input_handler)

        self.game_logic.add_object(player_game_object)
        self.game_logic.add_object(enemy_game_object)

        self.renderer.add_object(player_game_object_view)
        self.renderer.add_object(enemy_game_object_view)

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
        self.input_handler.handle_input(events)

    def update(self):
        self.handle_events()

        # обновление игровых объектов
        self.game_logic.update()
        
    def render(self):
        self.renderer.render()

    def run(self):
        while True:
            self.update()
            self.render()
            self.clock.tick(60)
