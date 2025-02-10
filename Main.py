import pygame

from Block import Block
from Shapes import Shape
from pygame.locals import *

cell_size = 20
screen_height = 20 * cell_size
screen_width = 10 * cell_size
pygame.init()
surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

    spawn_shape = Block(Shapes.random_shape(), 0, 0, cell_size, surface, 30)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and spawn_shape.rect.right < screen_height:
        spawn_shape.move(cell_size, 0)
    else if keys[pygame.K_LEFT] and spawn_shape.rect.x > 0:
        spawn_shape.move(-cell_size, 0)
    surface.fill((0, 0, 0))
    spawn_shape.draw()
    spawn_shape.update()
    pygame.display.flip()
    clock.tick(30)

