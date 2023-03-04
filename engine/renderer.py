import pygame

class Renderer:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen

        self.objects = []

    def render(self):
        self.screen.fill((255, 255, 255))

        for obj in self.objects:
            obj.render(self.screen)

        pygame.display.flip()

    def add_object(self, obj):
        self.objects.append(obj)
