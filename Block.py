from pygame.rect import Rect
from Square import Square

class Block():
    def __init__(self, matrix, x, y, block_size, color, surface, delay):
        self.matrix = matrix
        self.rect = Rect(x, y, len(matrix[0])*block_size, len(matrix)*block_size)
        self.surface = surface.subsurface(self.rect)
        self.squares = []
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                self.squares.append(Square(j*block_size, i*block_size, block_size, color, surface, delay))

        self.delay = delay

