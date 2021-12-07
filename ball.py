import pygame
import color

class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.radius = 10

    def draw(self, surface):
        pygame.draw.circle(surface, )