from screen import *
from soldier import *
import pygame
from consts import *
screen = display_soldier()


def main():
    running = True
    pos_x = 0
    pos_y = 0
    while running:
        # forloop through the event queue:
        for event in pygame.event.get():
            if event.type == pygame.K_KP_ENTER:
                # action - bombs exposure
                show_net(screen, SQUARE)
            elif event.type == pygame.K_UP:
                # action - step up
                move_up(pos_y)
            elif event.type == pygame.K_DOWN:
                # action - step down
                move_down(pos_y)
            elif event.type == pygame.K_RIGHT:
                # action - step right
                move_right(pos_x)
            elif event.type == pygame.K_LEFT:
                # action - step left
                move_left(pos_x)
            elif event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
