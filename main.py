import pygame
import game_field
from game_field import *
from screen import *
from consts import *
import soldier

def main():
    screen = display_flag()
    screen = soldier.display_solider(screen)
    running = True
    while running:
        # forloop through the event queue:
        for event in pygame.event.get():
            if event.type == pygame.K_KP_ENTER:
                # action - bombs exposure
                display_bomb(screen)
            elif event.type == pygame.K_UP:
                # action - step up
                a = 4
            elif event.type == pygame.K_DOWN:
                # action - step down
                a = 8
            elif event.type == pygame.K_RIGHT:
                # action - step right
                a = 8
            elif event.type == pygame.K_LEFT:
                # action - step left
                a = 6
            elif event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
