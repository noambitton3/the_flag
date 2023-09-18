import pygame
import random
import consts
from screen import *


# supposed to show a net
def show_net(screen, square):
    for x in range(consts.SCREEN_WIDTH):
        for y in range(consts.SCREEN_LENGTH):
            block = pygame.Rect(x * square, y * square, square, square)
            pygame.draw.rect(screen, GREEN, block, 1)
    pygame.display.flip()
    return

# need to show also the bombs and the soldier at night.
# also do not forget the time limit - just 1 second.


def create_bomb(bomb_size):
    bomb_ = pygame.image.load("mine.png")
    bomb = pygame.transform.scale(bomb_, BOMB_SIZE)
    return bomb


def display_bomb(screen):
    net_screen = show_net(screen, SQUARE)
    bomb = create_bomb(consts.BOMB_SIZE)
    for i in range(20):
        x = random.randint(0, 950)
        y = random.randint(0, 450)
        cord = (x, y)
        net_screen.blit(bomb, cord)
        pygame.display.update()
    return net_screen