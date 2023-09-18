import pygame
import random
from consts import *
from screen import *

def show_bombs(screen):
    block_size = 20
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_LENGTH):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(screen, GREEN, rect, 1)
    pygame.display.flip()