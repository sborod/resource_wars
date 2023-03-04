import pygame
from character import Character
from character_game_object import CharacterGameObject
from game_logic import GameLogic
from game_object_view import GameObjectView

from pygame_input_handler import PygameInputHandler
from pygame_renderer import PygameRenderer

tile_size = 20

class PygameGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        # создание окна игры
        self.renderer = PygameRenderer(width, height, self.screen)

        # создание игровых объектов и их декораторов
        player = Character("Player", 1, 10, 10, 5, 0, 1, 0, (0, 0))
        enemy = Character("Enemy", 1, 10, 10, 3, 0, 1, 0, (2, 0))

        player = CharacterGameObject(player)
        enemy = CharacterGameObject(enemy)

        player_game_object_view = GameObjectView(player, "circle", (0, 0, 255), tile_size, tile_size)
        enemy_game_object_view = GameObjectView(enemy, "rectangle", (255, 0, 0), tile_size, tile_size)

        # инициализация объектов для обработки пользовательского ввода
        self.input_handler = PygameInputHandler(player)

        # создание экземпляра GameLogic
        self.game_logic = GameLogic()

        self.game_logic.add_object(player)
        self.game_logic.add_object(enemy)

        self.renderer.add_object(player_game_object_view)
        self.renderer.add_object(enemy_game_object_view)

    def handle_events(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

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
