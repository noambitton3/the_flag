import random
import pygame
import consts
from consts import *
from game_field import *


def create_screen():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))
    screen.fill(GREEN)
    pygame.display.set_caption("the flag")
    pygame.display.flip()
    return screen


def create_bush(bush_size):
    bush_ = pygame.image.load("grass.png")
    bush = pygame.transform.scale(bush_, bush_size)
    return bush


def display_bushes():
    screen = create_screen()
    bush = create_bush(BUSH_SIZE)
    for i in range(20):
        x = random.randint(0, 950)
        y = random.randint(0, 450)
        cord = (x, y)
        screen.blit(bush, cord)
        pygame.display.update()
    return screen





