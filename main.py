import pygame
import game_field
from game_field import *
from screen import *
from consts import *
import soldier
screen = soldier.display_solider()

def main():
    # screen = display_flag()
    # screen = soldier.display_solider(screen)
    running = True
    soldier_x = 0
    soldier_y = 0
    while running:
        # forloop through the event queue:
        for event in pygame.event.get():
            if event.type == pygame.K_KP_ENTER:
                # action - bombs exposure
                display_bomb(screen)
            elif event.type == pygame.K_UP:
                # action - step up
                soldier.move_up(soldier_y)
                a = 4
            elif event.type == pygame.K_DOWN:
                # action - step down
                soldier.move_down(soldier_y)
                a = 8
            elif event.type == pygame.K_RIGHT:
                # action - step right
                soldier.move_right(soldier_x)
                a = 8
            elif event.type == pygame.K_LEFT:
                # action - step left
                soldier.move_left(soldier_x)
                a = 6
            elif event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
