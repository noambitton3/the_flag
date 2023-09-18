from screen import *


def create_soldier(soldier_width, soldier_length):
    soldier_ = pygame.image.load("soldier.png")
    soldier_size = (soldier_width, soldier_length)
    soldier = pygame.transform.scale(soldier_, soldier_size)
    return soldier


def display_soldier(screen):
    soldier = create_soldier(SOLDIER_WIDTH, SOLDIER_LENGTH)
    # initial position
    x = 0
    y = 0
    init_pos = (x, y)
    screen.blit(soldier, init_pos)
    pygame.display.update()
    return screen


# for every func need to display the new location of the soldier
def move_up(soldier_y):
    soldier_y -= 20
    return soldier_y


def move_down(soldier_y):
    soldier_y += 20
    return soldier_y


def move_right(soldier_x):
    soldier_x += 20
    return soldier_x


def move_left(soldier_x):
    soldier_x -= 20
    return soldier_x

