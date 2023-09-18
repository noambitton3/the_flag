import pygame
from screen import *


# supposed to show a net
def show_net(screen, square):
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_LENGTH):
            block = pygame.Rect(x * square, y * square, square, square)
            pygame.draw.rect(screen, GREEN, block, 1)
    pygame.display.flip()

# need to show also the bombs and the soldier at night.
# also do not forget the time limit - just 1 second.






