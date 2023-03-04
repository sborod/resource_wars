import pygame

from renderer import Renderer

class PygameRenderer(Renderer):
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.objects = []
        self.screen = screen

    def render(self):
        self.screen.fill((255, 255, 255))

        for obj in self.objects:
            obj.render(self.screen)

        pygame.display.flip()

    def add_object(self, obj):
        self.objects.append(obj)