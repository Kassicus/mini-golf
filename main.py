import pygame

import color
import maps

class Game():
    def __init__(self):
        self.width = 1200
        self.height = 900
        self.title = "Dual Mini Golf (Game Jam Inspired)"

        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(self.title)

        self.running = False

        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

    def start(self):
        self.running = True

        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(color.black)

    def update(self):
        pygame.display.update()
        self.clock.tick(30)

game = Game()
game.start()

pygame.quit()