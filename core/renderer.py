import pygame

from constants import COLOR_BLACK

class Renderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode((width, height))

        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def render(self):
        self.screen.fill(COLOR_BLACK)

        for obj in self.objects:
            obj.render(self.screen)

        pygame.display.flip()
