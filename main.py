import pygame
import game_field
from game_field import *
from screen import *
from consts import *
import soldier

screen = soldier.display_solider()


def main():
    put_text(consts.WHITE, screen)
    running = True
    soldier_x = 0
    soldier_y = 0
    while running:
        # forloop through the event queue:
        for event in pygame.event.get():
            if event.type == pygame.K_SPACE:
                # action - bombs exposure
                display_bomb(screen)
            elif event.type == pygame.K_UP:
                # action - step up
                screen.move_up(soldier_y)
                a = 5
            elif event.type == pygame.K_DOWN:
                # action - step down
                screen.move_down(soldier_y)
                a = 8
            elif event.type == pygame.K_RIGHT:
                # action - step right
                screen.move_right(soldier_x)
                a = 3
            elif event.type == pygame.K_LEFT:
                # action - step left
                screen.move_left(soldier_x)
                a = 6
            elif event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
