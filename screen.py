import pygame
from consts import *


def create_screen():
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))
    surface.fill(GREEN)
    pygame.display.flip()


def screen_stay():
    running = True
    while running:
        # for loop through the event queue
        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False
