from consts import *
from screen import *


def create_flag(flag_width, flag_length):
    flag_ = pygame.image.load("flag.png")
    flag_size = (flag_width, flag_length)
    flag = pygame.transform.scale(flag_, flag_size)
    return flag


def display_flag():
    screen = display_bushes()
    flag = create_flag(FLAG_WIDTH, FLAG_LENGTH)
    x = SCREEN_WIDTH - FLAG_WIDTH
    y = SCREEN_LENGTH - FLAG_LENGTH
    cord = (x, y)
    screen.blit(flag, cord)
    pygame.display.update()
    return screen


# supposed to show a net - there is a problem
def show_net(screen, square):
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_LENGTH):
            block = pygame.Rect(x * square, y * square, square, square)
            pygame.draw.rect(screen, GREEN, block, 1)
    pygame.display.flip()
    return

# need to show also the bombs and the soldier at night.
# also do not forget the time limit - just 1 second.


def create_bomb():
    bomb_ = pygame.image.load("mine.png")
    bomb = pygame.transform.scale(bomb_, BOMB_SIZE)
    return bomb


def display_bomb(screen):
    net_screen = show_net(screen, SQUARE)
    bomb = create_bomb()
    for i in range(20):
        x = random.randint(0, 950)
        y = random.randint(0, 450)
        cord = (x, y)
        net_screen.blit(bomb, cord)
        pygame.display.update()
    return net_screen






