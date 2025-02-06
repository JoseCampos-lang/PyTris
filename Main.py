import pygame

from OBlock import OBlock
from pygame.locals import *

CYAN = (0,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

cell_size = 20
screen_height = 20 * cell_size
screen_width = 10 * cell_size
pygame.init()
surface = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
o_block = OBlock(0,0,cell_size,surface,30)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]and o_block.rect.right < screen_height:
        o_block.move(cell_size, 0)
    if keys[pygame.K_LEFT] and o_block.rect.x>0:
        o_block.move(-cell_size, 0)
    surface.fill((0,0,0))
    o_block.draw()
    o_block.update()
    pygame.display.flip()
    clock.tick(30)