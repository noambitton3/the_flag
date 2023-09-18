import random
import pygame
import consts
from consts import *
from game_field import *

def create_screen():
    pygame.init()
    screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_LENGTH))
    screen.fill(consts.GREEN)
    pygame.display.set_caption("the flag")
    pygame.display.flip()
    return screen


def create_bush(bush_size):
    bush_ = pygame.image.load("grass.png")
    bush = pygame.transform.scale(bush_, bush_size)
    return bush


def display_bushes():
    screen = create_screen()
    bush = create_bush(consts.BUSH_SIZE)
    for i in range(20):
        x = random.randint(0, 950)
        y = random.randint(0, 450)
        cord = (x, y)
        screen.blit(bush, cord)
        pygame.display.update()
    return screen

def create_flag(flag_width, flag_length):
    flag_ = pygame.image.load("flag.png")
    flag_size = (flag_width, flag_length)
    flag = pygame.transform.scale(flag_, flag_size)
    return flag


def display_flag():
    screen = display_bushes()
    flag = create_flag(consts.FLAG_WIDTH, consts.FLAG_LENGTH)
    x = consts.SCREEN_WIDTH - consts.FLAG_WIDTH
    y = consts.SCREEN_LENGTH - consts.FLAG_LENGTH
    cord = (x, y)
    screen.blit(flag, cord)
    pygame.display.update()
    return screen