from screen import *
import pygame


def main():
    display_bushes()
    running = True
    while running:
        # forloop through the event queue:
        for event in pygame.event.get():
            if event.type == pygame.K_KP_ENTER:
                # action - boms exposure
                a = 10
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
