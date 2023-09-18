

# create_screen()
# screen_stay()

from screen import *
import pygame

gridDisplay = pygame.display.set_mode((1000, 500))
pygame.display.get_surface().fill((138, 201, 38))  # background

matrix = [[1, 1, 5, 1],
          [1, 0 ,0 ,1],
          [1 ,1 ,0 ,1],
          [1 ,1 ,1 ,1]]

grid_node_width = 20
grid_node_height = 20


def create_square(x, y, color):
    pygame.draw.rect(gridDisplay, color, [x, y, grid_node_width, grid_node_height])


pygame.display.update()
screen_stay()
