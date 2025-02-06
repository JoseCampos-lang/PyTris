import pygame.draw
from pygame.rect import Rect

class Square:
    def __init__(self, x, y, size, color, surface, delay):
        self.rect = Rect(x,y,size,size)
        self.color = color
        self.surface = surface
        self.turn = 0
        self.delay = delay

    def draw(self):
        pygame.draw.rect(self.surface, self.color,Rect(self.rect.x + 1,
         self.rect.y + 1,
         self.rect.width - 2,
         self.rect.height - 2)
)

    def update(self):
        if self.turn == self.delay:
            self.rect.y += self.rect.height
            self.turn = 0
        else:
            self.turn += 1