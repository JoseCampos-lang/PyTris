from Square import Square
from pygame.rect import Rect

YELLOW = (255,255,0)

class OBlock():
    def __init__(self, x, y, block_size, surface, delay):
        self.surface = surface
        self.delay = delay
        self.block_size = block_size
        self.blocks = []
        self.rect = Rect(x,y,block_size*2, block_size*2)
        self.turn = 0
        self.blocks.append(Square(x,y,self.block_size, YELLOW, surface, self.delay))
        self.blocks.append(Square(x + block_size,y,self.block_size, YELLOW, surface, self.delay))
        self.blocks.append(Square(x,y + block_size,self.block_size, YELLOW, surface, self.delay))
        self.blocks.append(Square(x + block_size,y + block_size,self.block_size, YELLOW, surface, self.delay))

    def update(self):
        if self.turn == self.delay and self.blocks[2].rect.bottom < self.surface.get_height():
            self.move(0, self.block_size)
            self.turn = 0
        else:
            self.turn += 1

    def draw(self):
        for block in self.blocks:
            block.draw()

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
        for block in self.blocks:
            block.rect.x += x
            block.rect.y += y