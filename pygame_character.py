import pygame
from character import Character

class PygameCharacter(Character):
    def update(self, events, is_player=False):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.move((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.move((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.move((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.move((1, 0))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.attack(self.get_clicked_enemy(pygame.mouse.get_pos()))
