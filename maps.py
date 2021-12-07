import pygame
import color

class Map():
    def __init__(self, x):
        self.x = x
        self.y = 0
        self.width = 600
        self.height = 900

    def draw(self, surface):
        pygame.draw.rect(surface, color.white, (self.x, self.y, self.width, self.height), 0)

    def update(self, events):
        pass