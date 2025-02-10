from pygame.rect import Rect
from Square import Square
from Shape import Shapes


class Block:
    def __init__(self, matrix, x, y, block_size, surface, delay):
        self.matrix = matrix
        self.rect = Rect(x, y, len(matrix[0]) * block_size, len(matrix) * block_size)
        self.surface = surface.subsurface(self.rect)
        self.squares = []
        match matrix:
            case Shapes.J:
                color = (0, 0, 255)
            case Shapes.L:
                color = (255, 165, 0)
            case Shapes.O:
                color = (255, 255, 0)
            case Shapes.I:
                color = (0, 255, 255)
            case Shapes.S:
                color = (0, 255, 0)
            case Shapes.Z:
                color = (255, 0, 0)
            case _:
                raise ValueError("NOT A VALID SHAPE!")
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                self.squares.append(
                    Square(
                        j * block_size,
                        i * block_size,
                        block_size,
                        color,
                        surface,
                        delay,
                    )
                )

        self.delay = delay

    def draw(self):
        for block in self.blocks:
            block.draw()

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
        for block in self.blocks:
            block.rect.x += x
            block.rect.y += y

    def rotate(self, cw):
        if cw is True:
            self.matrix = [list(row for row in list(zip(*self.matrix[::-1])))]
        else:
            self.matrix = [list(row for row in list(zip(*self.matrix)))][::-1]
